from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""A class containing common Selenium actions for web elements."""


class Events:

    """Initializes the Events class with a WebDriver instance."""
    def __init__(self, driver):
        self.driver = driver

    """Clicks on the web element specified by the locator."""
    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    """Enters text into the web element specified by the locator."""
    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    """Gets the text of the web element specified by the locator."""
    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    """Checks if the web element specified by the locator is enabled."""
    def is_enabled(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    """Waits until the title of the page matches the specified title."""
    def get_title(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title

    """Scrolls the page to bring the web element specified by the locator into view."""
    def scroll_to_element(self, by_locator):
        self.driver.execute_script("window.scrollBy(0, arguments[0].offsetTop);", by_locator)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
