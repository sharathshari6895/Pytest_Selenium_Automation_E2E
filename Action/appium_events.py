from appium.webdriver.webdriver import WebDriver

""" A class containing common Appium actions for mobile elements. """


class AppiumEvents:

    """Initializes the AppiumEvents class with a WebDriver instance and sets implicit wait timeout."""
    def __init__(self, driver: WebDriver, implicit_wait_timeout=20):
        self.driver = driver
        self.driver.implicitly_wait(implicit_wait_timeout)

    """Clicks on the mobile element specified by the locator."""
    def do_click(self, by_locator):
        self.wait_for_element(by_locator).click()

    """Enters text into the mobile element specified by the locator."""
    def do_send_keys(self, by_locator, text):
        self.wait_for_element(by_locator).send_keys(text)

    """Gets the text of the mobile element specified by the locator."""
    def get_element_text(self, by_locator):
        element = self.wait_for_element(by_locator)
        return element.text

    """Checks if the mobile element specified by the locator is enabled."""
    def is_enabled(self, by_locator):
        element = self.wait_for_element(by_locator)
        return element.is_enabled()

    """Scrolls the page to bring the mobile element specified by the locator into view."""
    def scroll_to_element(self, by_locator):
        element = self.wait_for_element(by_locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    """Waits for the mobile element specified by the locator to be present and returns it."""
    def wait_for_element(self, by_locator):
        element = self.driver.find_element(*by_locator)
        return element
