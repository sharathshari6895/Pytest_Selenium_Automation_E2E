import time

import allure
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from Action.appium_events import AppiumEvents
import logging
import pyautogui

""" A class representing automation of a favorite recipe feature in the BigOven application using Appium.
   Inherits from AppiumEvents for common Appium actions. """


class BigOvenFavoriteRecipe(AppiumEvents):
    signIn_button = (
        By.XPATH, "//android.widget.LinearLayout/android.widget.FrameLayout/android.widget.TextView[@text='Sign in']")
    email_input = (By.XPATH, "//android.widget.EditText[@resource-id='com.bigoven.android:id/email']")
    password_input = (By.XPATH, "//android.widget.EditText[@resource-id='com.bigoven.android:id/password']")
    big_oven_logo = (By.XPATH,
                     "//android.view.ViewGroup[@resource-id='com.bigoven.android:id/scrollingToolbar']/android.widget.ImageView")
    search_icon_locator = (By.XPATH, "	//android.widget.Button[@content-desc='Search All Recipes']")
    my_recipes_locator = (By.XPATH, "//android.widget.LinearLayout[@content-desc='My Recipes']")
    search_input_locator = (By.XPATH, "//android.widget.AutoCompleteTextView[@text='Search 1,000,000+ Recipes']")
    search_recipe = (
        By.XPATH, "//android.widget.AutoCompleteTextView[@resource-id='com.bigoven.android:id/searchBarText']")
    select_favorites_locator = (By.XPATH, "//android.widget.TextView[@text='Favorites']")
    select_recipe_locator = (By.XPATH,
                             "(//androidx.recyclerview.widget.RecyclerView[@resource-id = 'com.bigoven.android:id/recyclerview']/android.widget.FrameLayout/  android.widget.RelativeLayout)[1]")
    add_to_favourite_locator = (
        By.XPATH, "//android.widget.ImageButton[@content-desc='Tap to save this recipe to Favorites folder']")
    navigate_to_home_from_favourite_locator = (
        By.XPATH,
        "//android.view.ViewGroup[@resource-id='com.bigoven.android:id/appToolbar']/android.widget.ImageButton")
    navigate_to_home_from_recipe_locator = (
        By.XPATH,
        "//android.view.ViewGroup[@resource-id = 'com.bigoven.android:id/appToolbar']/android.widget.ImageButton")
    navigate_to_home_from_search_field_locator = (
        By.XPATH, "//android.widget.ImageButton[@content-desc= 'Navigate up']")
    get_ideas_text_locator = (By.XPATH, "//android.widget.LinearLayout[@content-desc='Get Ideas']")
    check_selected_recipe_locator = (By.XPATH, "(//android.widget.TextView[@text='Dosa'])[1]")
    check_second_selected_recipe_locator = (By.XPATH, "(//android.widget.TextView[@text='Dosa'])[2]")
    check_inspired_text_locator = (
        By.XPATH, "(//android.widget.TextView[@resource-id ='com.bigoven.android:id/header_text'])[1]")
    header_three_dots_locator = (By.XPATH, "//android.widget.ImageView[@content-desc='More options']")
    settings_locator = (By.XPATH, "//android.widget.TextView[@text='Settings']")
    sign_out_locator = (By.XPATH, "(//android.widget.TextView[@resource-id='android:id/title'])[8]/..")
    confirm_sign_out_locator = (By.XPATH, "//android.widget.Button[@resource-id='android:id/button1']")
    select_tea_recipe_locator = (By.XPATH,
                                 "//android.widget.TextView[@resource-id='com.bigoven.android:id/title' and @text='Russian Tea (spiced Tea)']")

    """Initializes the BigOvenFavoriteRecipe with a WebDriver instance."""
    def __init__(self, driver):
        super().__init__(driver)

    """Finds and returns a single web element based on the given locator."""
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    """Clicks on the sign-in button."""
    def click_sign_in_button(self):
        sign_in_button = self.driver.find_element(*self.signIn_button)
        sign_in_button.click()

    """Logs out from the BigOven application."""
    def logout_from_big_oven(self):
        self.do_click(self.header_three_dots_locator)
        self.do_click(self.settings_locator)
        self.do_click(self.sign_out_locator)
        self.do_click(self.confirm_sign_out_locator)

    """Waits for the BigOven logo to become visible on the screen."""
    def wait_for_logo_visibility(self):
        try:
            self.find_element(self.big_oven_logo)
            return True
        except NoSuchElementException:
            logging.error("bigOven_logo is not present")
            return False

    """Checks for the visibility of 'Inspired' text."""
    def check_for_inspiredtext_visibility(self):
        try:
            self.find_element(self.check_inspired_text_locator)
            return True
        except NoSuchElementException:
            logging.error("check_inspired_text_locator is not present")
            return False

    """Enters the username and password in the sign-in form."""
    def signin_details(self, username, password):
        self.do_send_keys(self.email_input, username)
        self.do_send_keys(self.password_input, password)

    """Performs sign-in with the provided email and password."""
    def perform_sign_in(self, email, password):
        self.click_sign_in_button()
        self.signin_details(email, password)
        self.click_sign_in_button()

    """Searches for a recipe by name."""
    def search_recipe_name(self, recipe_name):
        self.do_send_keys(self.search_recipe, recipe_name)
        pyautogui.press('enter')
        time.sleep(3)

    """Adds a recipe to the favorite list."""
    def add_recipie_to_favorite_list(self):
        self.do_click(self.select_recipe_locator)
        self.do_click(self.add_to_favourite_locator)
        self.do_click(self.navigate_to_home_from_favourite_locator)
        self.do_click(self.navigate_to_home_from_search_field_locator)
        self.do_click(self.my_recipes_locator)
        self.do_click(self.select_favorites_locator)

    def add_recipie_to_favorite_lists(self):
        self.do_click(self.select_tea_recipe_locator)
        self.do_click(self.add_to_favourite_locator)
        self.do_click(self.navigate_to_home_from_favourite_locator)
        self.do_click(self.navigate_to_home_from_search_field_locator)
        self.do_click(self.my_recipes_locator)
        self.do_click(self.select_favorites_locator)

    """Clicks on the search input field."""
    def click_on_search_input(self):
        self.do_click(self.search_icon_locator)
        self.do_click(self.search_input_locator)

    """Checks if Recipe is present."""
    def is_checking_recipe_presence(self):
        self.find_element(self.check_selected_recipe_locator)
        return True

    """Checks if a recipe is still present after removing."""
    def checking_recipe_presence_after_removing(self):
        try:
            time.sleep(1)
            self.find_element(self.select_tea_recipe_locator)
            logging.error("recipe is still present after removing")
            return False
        except NoSuchElementException:
            logging.info("recipe is not present after removing")
            return True

    """Removes a recipe from the favorite list."""
    def remove_recipe_from_favorite(self):
        self.do_click(self.select_tea_recipe_locator)
        self.do_click(self.add_to_favourite_locator)
        self.do_click(self.navigate_to_home_from_favourite_locator)

    """Navigates to the homepage of the application."""
    def navigate_to_homepage(self):
        self.do_click(self.navigate_to_home_from_search_field_locator)
