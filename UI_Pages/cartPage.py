import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Action.action import Events
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, InvalidArgumentException

"""A class representing the cart page functionality of a web application.
   Inherits from Events for common Selenium actions. """


class CartPage(Events):
    # Locators for various elements on the page
    selectProduct_locator = (By.XPATH, "//img[@alt='Sauce Labs Backpack']")
    addToCartBtn_locator = (By.XPATH, "//button[text()='Add to cart']")
    removeFromCartBtn_locator = (By.XPATH, "//button[text()='Remove']")
    shoppingCartBadge_locator = (By.XPATH, "//span[@class='shopping_cart_badge']")
    shoppingCartIcon_locator = (By.XPATH, "//a[@class='shopping_cart_link']")
    description_div_locator = (By.XPATH, "//div[@class='inventory_details_desc_container']")
    product_name_div_locator = (By.XPATH, "//div[text()='Sauce Labs Backpack']")
    check_productName_in_cart_locator = (By.XPATH, "//div[@id='cart_contents_container']")
    toggle_menu_locator = (By.XPATH, "//button[@id='react-burger-menu-btn']")
    logout_button_locator = (By.XPATH, "//a[@id='logout_sidebar_link']")
    cart_items_locator = (By.XPATH, "//div[@class='cart_item']")
    product_name_xpath = ".//div[@class='inventory_item_name']"
    remove_button_xpath = ".//button[text()='Remove']"

    """Initializes the CartPage with a WebDriver instance."""
    def __init__(self, driver):
        super().__init__(driver)

    """Finds and returns a single web element based on the given locator."""
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    """Finds and returns a list of web elements based on the given locator."""
    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    """Selects a product from the product list."""
    def select_product(self):
        self.do_click(self.selectProduct_locator)

    """Adds the selected product to the shopping cart."""
    def add_to_cart(self):
        try:
            add_to_cart_button = self.find_element(self.addToCartBtn_locator)
            assert add_to_cart_button.is_displayed(), "Add to cart button is not displayed"
            add_to_cart_button.click()
            print("Clicked on Add to cart")
        except NoSuchElementException:
            print("Add to cart button is not found")

    """Clicks on the shopping cart icon."""
    def click_cart_icon(self):
        self.do_click(self.shoppingCartIcon_locator)

    """Checks if the specified product is present in the cart."""
    def checking_productIn_cart(self, product_name):
        description_div_element = self.find_element(self.check_productName_in_cart_locator)
        assert product_name in description_div_element.text, "Product not found in cart"
        print("Add to Cart successfully")

    """Logging out from the web page."""
    def logout_page(self):
        self.do_click(self.toggle_menu_locator)
        self.do_click(self.logout_button_locator)

    """Checks if the shopping cart is empty."""
    def is_shopping_cart_empty(self):
        try:
            self.driver.find_element(*self.shoppingCartBadge_locator)
            return False  # Shopping cart badge found, indicating cart is not empty
        except NoSuchElementException:
            print("Shopping cart badge not found.")
            return True

    """Removes the specified item from the shopping cart."""
    def remove_item_from_cart(self, product_name):
        try:
            self.do_click(self.shoppingCartIcon_locator)
            cart_items = self.find_elements(self.cart_items_locator)
            for cart_item in cart_items:
                product_name_in_cart = cart_item.find_element(By.XPATH, self.product_name_xpath).text
                if product_name == product_name_in_cart:
                    remove_button = cart_item.find_element(By.XPATH, self.remove_button_xpath)
                    remove_button.click()
                    print("CartItem is removed")
                    return  # Exit the method after removing the item
        except NoSuchElementException as e:
            print(f"Element not found: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

    """Waits for the product element to be present on the page."""
    def wait_for_product_element(self, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(self.product_name_div_locator)
            )
            print("Product 'Sauce Labs Backpack' is present")
            return True
        except:
            print("Product 'Sauce Labs Backpack' is not present within the timeout period")
            return False

    """Combines the select, add_to_cart, and click_cart_icon methods to add a product to the cart."""
    def add_product_to_cart(self):
        self.select_product()
        self.add_to_cart()
        self.click_cart_icon()
