import os
import json
import allure
import requests
import configparser
import pytest
import logging
from axe_selenium_python import Axe
from selenium import webdriver
from typing import Dict, Any
from appium.webdriver.appium_service import AppiumService
from appium.options.common import AppiumOptions
from MobilePages.bigoven_favorite_recipes import BigOvenFavoriteRecipe
from MobilePages.bigoven_adding_new_recipe import BigOvenRecipeManager
from UI_Pages.cartPage import CartPage
from UI_Pages.checkoutPage import CheckoutPage
from UI_Pages.loginPage import LoginPage
#
from Utils.file_util import current_dir, config_path, ui_data_path, mobile_data_path, assertion_data_path, api_data_path





@pytest.fixture(scope='function')
def api_config_from_ini():
    return read_config_data(config_path, 'API')


def read_config_data(file_path, section):
    config = configparser.ConfigParser()
    config.read(file_path)
    if section == 'API':
        if 'API' in config:
            return dict(config['API'])
        else:
            raise ValueError("Section 'API' not found in the config file.")
    elif section == 'UI':
        if 'UI' in config:
            return dict(config['UI'])
        else:
            raise ValueError(f"Section 'UI' not found in the config file.")
    elif section == 'Mobile':
        if 'Mobile' in config:
            mobile_config = config['Mobile']
            return mobile_config
        else:
            raise ValueError("Section 'Mobile' not found in the config file.")
    elif section == 'Accessibility':
        if 'Accessibility' in config:
            return dict(config['Accessibility'])
        else:
            raise ValueError("Section 'Accessibility' not found in the config file.")
    else:
        raise ValueError(f"Section '{section}' is not supported.")


# Fixture to obtain an authentication token for API requests
@pytest.fixture(scope='function')
def auth_token(api_data_fixture, api_config_from_ini):
    api_config = api_config_from_ini
    response = requests.post(api_config['api_url'] + api_config['auth_end_point'],
                             json=api_data_fixture.get('auth_payload', {}))
    return response.json()["token"]


# Fixture to obtain a booking ID created through API requests
@pytest.fixture(scope='function')
def created_booking_id(api_data_fixture, auth_token, api_config_from_ini):
    api_config = api_config_from_ini
    response = requests.post(api_config['api_url'] + api_config['booking_base_end_point'],
                             json=api_data_fixture.get("booking_data", {}), headers={'Cookie': 'token=' + auth_token})
    assert response.status_code == 200, f"Failed to create booking. Status code: {response.status_code}"
    return response.json().get("bookingid", '')


import sys
from unittest.mock import MagicMock

# Mock pyautogui
sys.modules['pyautogui'] = MagicMock()
sys.modules['mouseinfo'] = MagicMock()





# Fixture to initialize Appium pages for testing
@pytest.fixture(scope="function")
def setup_appium_pages(appium_driver_setup):
    appium_driver = appium_driver_setup
    big_oven_favoritePage = BigOvenFavoriteRecipe(appium_driver)
    big_oven_new_recipe = BigOvenRecipeManager(appium_driver)
    return appium_driver, big_oven_favoritePage, big_oven_new_recipe


# Fixture to set up pages for each test function
@pytest.fixture(scope="function")
def setup_pages(init_driver):
    driver = init_driver
    login_page = LoginPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)
    return driver, login_page, cart_page, checkout_page


@pytest.fixture
def accessibility_driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def run_accessibility_test(accessibility_driver):
    def _run_accessibility_test(url):
        accessibility_driver.get(url)
        axe = Axe(accessibility_driver)
        axe.inject()
        results = axe.run()
        return results

    return _run_accessibility_test


def read_json_file(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
    return data


@pytest.fixture
def ui_data():
    return read_json_file(ui_data_path)


@pytest.fixture
def assertion_data():
    return read_json_file(assertion_data_path)


@pytest.fixture(scope='function')
def api_data_fixture():
    return read_json_file(api_data_path)


@pytest.fixture
def mobile_data():
    return read_json_file(mobile_data_path)


#
# # Fixture to set up logging configuration before each test
@pytest.fixture(scope='function', autouse=True)
def logger_setup(request):
    # pytest_config = read_config_data(config_path, 'Report_portal')
    logger_name = "root"
    root_logger = logging.getLogger(logger_name)
    root_logger.setLevel(logging.INFO)
    formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(name)s : %(message)s',
                                  datefmt='%m/%d/%Y %I:%M:%S %p')
    # Adding console handler for displaying logs in the console
    consoleHandler = logging.StreamHandler()
    consoleHandler.setFormatter(formatter)
    root_logger.addHandler(consoleHandler)
    fileHandler = None
    log_folder = os.path.abspath(
        os.path.join(current_dir, '..', 'Log'))
    try:
        os.makedirs(log_folder, exist_ok=True)
        log_file = os.path.join(log_folder, 'test_logs.log')
        fileHandler = logging.FileHandler(log_file)
        fileHandler.setFormatter(formatter)
        root_logger.addHandler(fileHandler)
    except Exception as e:
        print(f"Error creating log folder or file: {e}")

    urllib3_logger = logging.getLogger('urllib3')
    urllib3_logger.setLevel(logging.ERROR)
    consoleHandler.setLevel(logging.ERROR)
    yield
    # Cleaning up log handlers to avoid duplicate log entries
    root_logger.removeHandler(consoleHandler)
    if fileHandler:
        root_logger.removeHandler(fileHandler)
        fileHandler.close()


# Flag to track whether a test has already failed and a screenshot has been captured
test_failed = False


@pytest.fixture(scope="function")
def init_driver(request):
    global test_failed  # Declare the global variable
    global driver
    browser = request.node.callspec.params.get("browser", None)
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument('--log-level=3')
        driver = webdriver.Chrome(options=options)
    elif browser == "edge":
        options = webdriver.EdgeOptions()
        driver = webdriver.Edge(options=options)
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    ui_config = read_config_data(config_path, 'UI')
    if not ui_config or 'base_url' not in ui_config:
        raise ValueError("BASE_URL not found in the config file.")
    base_url = ui_config['base_url']
    driver.maximize_window()
    driver.get(base_url)
    request.cls.driver = driver

    try:
        yield driver
    finally:
        if request.session.testsfailed > 0 and not test_failed:
            screenshot_path = capture_screenshot(driver, "ui_test_failure", folder_name="ui_automation")
            allure.attach.file(screenshot_path, name="Screenshot", attachment_type=allure.attachment_type.PNG)
            test_failed = True
        print("Closing the driver...")
        driver.quit()


# Fixture for Appium driver setup
@pytest.fixture(scope="function")
def appium_driver_setup(request):
    mobile_config = read_config_data(config_path, 'Mobile')
    mobile_data = read_json_file(mobile_data_path)
    appium_service = AppiumService()
    appium_service.start()
    test_failed = False  # Initialize the test_failed variable

    cap: Dict[str, Any] = {
        "deviceName": mobile_config['deviceName'],
        "platformName": mobile_config['platformName'],
        "automationName": mobile_config['automationName'],
        "appActivity": mobile_config['appActivity'],
        "appPackage": mobile_config['appPackage'],
        "auto_accept_alerts": mobile_config['auto_accept_alerts'],
        "unhandled_prompt_behavior": mobile_config['unhandled_prompt_behavior'],
        "timeout": mobile_config['timeout'],
        "noReset": mobile_config['noReset']
    }

    driver = webdriver.Remote(mobile_config['appium_server_url'], options=AppiumOptions().load_capabilities(cap))

    try:
        yield driver
    finally:
        if request.session.testsfailed > 0 and not test_failed:
            screenshot_path = capture_screenshot(driver, "mobile_test_failure", folder_name="mobile_automation",
                                                 target_size=(250, 500))
            allure.attach.file(screenshot_path, name="Screenshot", attachment_type=allure.attachment_type.PNG)
            test_failed = True

        driver.quit()
        appium_service.stop()


import os
from PIL import Image


def capture_screenshot(driver, screenshot_name, folder_name=None , target_size=None):
    print("Test case failed. Capturing screenshot...")
    screenshot_dir = os.path.join(os.getcwd(), "Screenshots")
    if folder_name:
        screenshot_dir = os.path.join(screenshot_dir, folder_name)
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)

    screenshot_number = len(os.listdir(screenshot_dir)) + 1
    screenshot_file = os.path.join(screenshot_dir, f"{screenshot_name}_{screenshot_number}.png")

    driver.save_screenshot(screenshot_file)
    if target_size:
        # Resize the screenshot to the target size
        img = Image.open(screenshot_file)
        img = img.resize(target_size, resample=Image.BILINEAR)  # Use the integer representation
        img.save(screenshot_file)

    print(f"Screenshot captured: {screenshot_file}")
    return screenshot_file
