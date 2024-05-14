from selenium.webdriver.common.by import By
from Action.action import Events
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

""" A class representing the login page functionality of a web application.
   Inherits from Events for common Selenium actions."""


class LoginPage(Events):
    userName_input = (By.XPATH, "//input[@id='user-name']")
    password_input = (By.XPATH, "//input[@id='password']")
    signIn_button = (By.XPATH, "//input[@id='login-button']")
    h3_locator = (By.XPATH, "//h3[text()='Epic sadface: Username and password do not match any user in this service']")

    """Method to wait for the error message to be displayed"""
    def wait_for_error_element(self, timeout=20):
        try:
            h3_locator_element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(self.h3_locator))
            return h3_locator_element
        except TimeoutException:
            print("Timed out waiting for h3 element to be present.")
            return None

    """Initializes the LoginPage with a WebDriver instance."""
    def __init__(self, driver):
        super().__init__(driver)

    """Inputs login credentials and clicks sign-in. Parameters: username (str), password (str)."""
    def click_login(self, username, password):
        self.do_send_keys(self.userName_input, username)
        self.do_send_keys(self.password_input, password)
        self.do_click(self.signIn_button)
