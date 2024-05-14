import time
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from Action.appium_events import AppiumEvents
import logging
import pyautogui

""" A class representing a recipe manager application automation using Appium.
   Inherits from AppiumEvents for common Appium actions. """


class BigOvenRecipeManager(AppiumEvents):
    my_recipe_locator = (By.XPATH, "//android.widget.LinearLayout[@content-desc = 'My Recipes']")
    plus_button_locator = (By.XPATH, "//android.widget.ImageButton[@resource-id='com.bigoven.android:id/fab']")
    type_in_recipe_locator = (By.XPATH,
                              "//android.widget.LinearLayout[@resource-id='com.bigoven.android:id/type_it_in_fab']/android.widget.ImageButton")
    add_title_input_locator = (By.XPATH, "//android.widget.EditText[@resource-id='titleInput']")
    add_ingredient_input_locator = (By.XPATH, "//android.widget.EditText[@resource-id='ingredientsInput']")
    instruction_input_locator = (By.XPATH, "//android.widget.EditText[@resource-id='instructionsInput']")
    comparing_text_value_locator = (By.XPATH,
                                    "//android.view.View[@resource-id='fb-root']/parent::android.webkit.WebView/android.view.View/android.widget.TextView[2]")
    add_recipe_btn_locator = (By.XPATH, "//android.widget.Button[@text='Add Recipe »']")
    navigate_to_home_from_selected_recipe_locator = (
        By.XPATH,
        "//android.view.ViewGroup[@resource-id = 'com.bigoven.android:id/appToolbar']/android.widget.ImageButton")
    all_recipe_locator = (By.XPATH,
                          "//android.widget.HorizontalScrollView[@resource-id='com.bigoven.android:id/tabs']/android.widget.LinearLayout/android.widget.LinearLayout[1]")
    search_icon_locator = (By.XPATH, "	//android.widget.Button[@content-desc='Search All Recipes']")
    search_input_locator = (By.XPATH, "//android.widget.AutoCompleteTextView[@text='Search 1,000,000+ Recipes']")
    search_recipe = (
        By.XPATH, "//android.widget.AutoCompleteTextView[@resource-id='com.bigoven.android:id/searchBarText']")
    checking_recipe_presence_locator = (
        By.XPATH, "//android.widget.TextView[@resource-id='com.bigoven.android:id/title']")
    navigate_to_home_from_search_field_locator = (
        By.XPATH, "//android.widget.ImageButton[@content-desc= 'Navigate up']")

    """Initializes the BigOvenRecipeManager with a WebDriver instance."""
    def __init__(self, driver):
        super().__init__(driver)

    """ Adds a new recipe with the provided title, ingredients, and preparation instructions."""
    def adding_new_recipe(self, title, ingradients, preparation):
        self.do_click(self.my_recipe_locator)
        self.do_click(self.plus_button_locator)
        self.do_click(self.type_in_recipe_locator)
        self.do_send_keys(self.add_title_input_locator, title)
        self.do_send_keys(self.add_ingredient_input_locator, ingradients)
        self.do_send_keys(self.instruction_input_locator, preparation)
        time.sleep(1)
        self.do_click(self.add_recipe_btn_locator)

    """ Validates the title of the last added recipe."""
    def validate_added_recipe_title(self, expected_title):
        actual_title = self.driver.find_element(*self.comparing_text_value_locator).text
        assert expected_title in actual_title, f"Title does not match the provided title. Expected: {expected_title}, Actual: {actual_title}"
        return True

    """ Checks the presence of a newly added recipe. """
    def checkingThePresenceOfNewRecipe(self, title):
        self.do_click(self.navigate_to_home_from_selected_recipe_locator)
        self.do_click(self.all_recipe_locator)
        self.do_click(self.search_icon_locator)
        self.do_click(self.search_input_locator)
        self.do_send_keys(self.search_recipe, title)
        time.sleep(3)
        # self.driver.press_keycode(84)
        pyautogui.press('enter')
        actualText = self.driver.find_element(*self.checking_recipe_presence_locator).text
        assert title in actualText, "Expected title '{}' not found in actual text '{}'".format(title, actualText)
        self.do_click(self.navigate_to_home_from_search_field_locator)
