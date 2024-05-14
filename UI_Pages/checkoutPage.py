from selenium.common import NoSuchElementException
from Action.action import Events
from selenium.webdriver.common.by import By
import logging

""" A class representing the checkout page functionality of a web application.
    Inherits from Events for common Selenium actions. """


class CheckoutPage(Events):
    shoppingCartIcon_locator = (By.XPATH, "//a[@class='shopping_cart_link']")
    checkoutBtn_locator = (By.XPATH, "//button[text()='Checkout']")
    firstName_input = (By.XPATH, "//input[@id='first-name']")
    lastName_input = (By.XPATH, "//input[@id='last-name']")
    zipCode_input = (By.XPATH, "//input[@id='postal-code']")
    continue_checkout_btn = (By.XPATH, "//input[@id='continue']")
    finish_checkout_btn = (By.XPATH, "//button[@id='finish']")
    dropdown_locator = (By.XPATH, "//select[@class='product_sort_container']")
    select_option = (By.XPATH, "//option[@value='lohi']")
    product_price_locator = (By.XPATH, "//div[@class='inventory_item_price']")
    thank_you_locator = (By.XPATH, "//h2[text()='Thank you for your order!']")

    """Initializes the CheckoutPage with a WebDriver instance."""
    def __init__(self, driver):
        super().__init__(driver)

    """Clicks on the shopping cart icon."""
    def click_cart_icon(self):
        self.do_click(self.shoppingCartIcon_locator)

    """Clicks on the checkout button."""
    def click_checkout(self):
        self.do_click(self.checkoutBtn_locator)

    """Enters the checkout details - first name, last name, and zip code."""
    def checkout_details(self, firstname, lastname, zipcode):
        self.do_send_keys(self.firstName_input, firstname)
        self.do_send_keys(self.lastName_input, lastname)
        self.do_send_keys(self.zipCode_input, zipcode)

    """Clicks on the continue checkout button."""
    def continue_checkout(self):
        self.do_click(self.continue_checkout_btn)

    """Clicks on the finish checkout button."""
    def finish_checkout(self):
        self.do_click(self.finish_checkout_btn)

    """Selects an option from the dropdown menu."""
    def select_dropdown(self):
        self.do_click(self.dropdown_locator)
        self.do_click(self.select_option)

    """ Compares the prices of the first two products on the page.Prints a message indicating whether
        the price of the second product is higher or lower than the first. """
    def compare_product_prices(self):
        price_elements = self.driver.find_elements(*self.product_price_locator)
        prices = [price_element.text.strip('$') for price_element in price_elements[:2]]
        numeric_prices = [float(price) for price in prices]
        if numeric_prices[1] >= numeric_prices[0]:
            print("The price of the second product is higher or equal to the first product.")
        else:
            print("The price of the second product is lower than the first product.")

    """ Checks if the checkout button text is visible on the page.
        Returns: bool: True if the checkout button text is visible, False otherwise. """
    def is_checkout_text_visible(self):
        try:
            checkout_text_element = self.driver.find_element(*self.checkoutBtn_locator)
            return checkout_text_element.is_displayed()
        except NoSuchElementException:
            return False

    """ Checks if the 'Thank you for your order!' message is visible on the page.
    Returns: bool: True if the message is visible, False otherwise. """
    def is_thank_you_message_visible(self):
        try:
            thank_you_element = self.driver.find_element(*self.thank_you_locator)
            return thank_you_element.is_displayed()
        except NoSuchElementException:
            return False

    """ Checks if the dropdown menu is visible on the page.
        Returns:bool: True if the dropdown menu is visible, False otherwise. """
    def is_dropdown_visible(self):
        try:
            dropdown_element = self.driver.find_element(*self.dropdown_locator)
            return dropdown_element.is_displayed()
        except NoSuchElementException:
            return False
