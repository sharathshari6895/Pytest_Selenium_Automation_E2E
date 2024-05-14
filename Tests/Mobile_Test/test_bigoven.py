import allure

from Tests.configtest import appium_driver_setup
import pytest
import logging
from Tests.configtest import mobile_data, logger_setup, setup_appium_pages
from Utils import util


class TestBigOven:

    """Logging in with valid credentials, Searching for a recipe, Selecting a recipe,
    adding the recipe to favorites, and checking if the recipe is added to the favorites"""
    @pytest.mark.run(order=12)
    @allure.severity(allure.severity_level.NORMAL)
    def test_adding_recipe_to_favorites(self, appium_driver_setup, setup_appium_pages, mobile_data, logger_setup):
        logging.getLogger("root").info("Starting test_adding_recipe_to_favorites")
        allure.attach('Starting test_adding_recipe_to_favorites', attachment_type=allure.attachment_type.TEXT)
        appium_driver, big_oven_favoritePage, _ = setup_appium_pages
        big_oven_favoritePage.perform_sign_in(mobile_data["Email"], mobile_data["password"])
        assert big_oven_favoritePage.wait_for_logo_visibility(), "Logo is not visible after login"
        logging.getLogger("root").info("Login Successful")
        allure.attach('Login Successful', attachment_type=allure.attachment_type.TEXT)
        big_oven_favoritePage.click_on_search_input()
        assert big_oven_favoritePage.check_for_inspiredtext_visibility(), "check_inspired_text_locator is not present"
        big_oven_favoritePage.search_recipe_name(mobile_data["recipe2"])
        big_oven_favoritePage.add_recipie_to_favorite_list()
        assert big_oven_favoritePage.is_checking_recipe_presence(), "Element is not present"
        logging.getLogger("root").info("Recipe added successfully to the Favorite List")
        allure.attach('Recipe added successfully to the Favorite List', attachment_type=allure.attachment_type.TEXT)
        big_oven_favoritePage.navigate_to_homepage()
        big_oven_favoritePage.logout_from_big_oven()
        logging.getLogger("root").info("Ending test_adding_recipe_to_favorites")
        allure.attach('Ending test_adding_recipe_to_favorites', attachment_type=allure.attachment_type.TEXT)

    """Logging in with valid credentials, Searching for a recipe, Selecting a recipe, adding the recipe to favorites,
     checking if the recipe is added to the favorites, Removing the recipe from favorites
      and Checking if the recipe is removed from favorites"""
    # @pytest.mark.run(order=13)
    # @allure.severity(allure.severity_level.CRITICAL)
    # def test_remove_recipe_from_favorites(self, appium_driver_setup, setup_appium_pages, mobile_data):
    #     logging.getLogger("root").info("Starting  test_remove_recipe_from_favorites")
    #     allure.attach('Starting test_remove_recipe_from_favorites', attachment_type=allure.attachment_type.TEXT)
    #     appium_driver, big_oven_favoritePage, _ = setup_appium_pages
    #     big_oven_favoritePage.perform_sign_in(mobile_data["Email"], mobile_data["password"])
    #     assert big_oven_favoritePage.wait_for_logo_visibility(), "Logo is not visible after login"
    #     logging.getLogger("root").info("Login Successful")
    #     allure.attach('Login Successful', attachment_type=allure.attachment_type.TEXT)
    #     big_oven_favoritePage.click_on_search_input()
    #     assert big_oven_favoritePage.check_for_inspiredtext_visibility(), "check_inspired_text_locator is not present"
    #     big_oven_favoritePage.search_recipe_name(mobile_data["recipe1"])
    #     big_oven_favoritePage.add_recipie_to_favorite_lists()
    #     logging.getLogger("root").info("Recipe added successfully to the Favorite List")
    #     allure.attach('Recipe added successfully to the Favorite List', attachment_type=allure.attachment_type.TEXT)
    #     big_oven_favoritePage.remove_recipe_from_favorite()
    #     assert big_oven_favoritePage.checking_recipe_presence_after_removing(), "recipe is present after removing"
    #     logging.getLogger("root").info("Recipe Removed successfully to the Favorite List")
    #     allure.attach('Recipe Removed successfully to the Favorite List', attachment_type=allure.attachment_type.TEXT)
    #     big_oven_favoritePage.navigate_to_homepage()
    #     big_oven_favoritePage.logout_from_big_oven()
    #     logging.getLogger("root").info("Ending test_remove_recipe_from_favorites")
    #     allure.attach('Ending test_remove_recipe_from_favorites', attachment_type=allure.attachment_type.TEXT)
    #
    # # """Logging in with valid credentials, adding a new recipe, checking the title of the recipe after adding,
    # # and verifying the presence of the recipe by searching in the search bar"""
    # @pytest.mark.run(order=14)
    # @allure.severity(allure.severity_level.CRITICAL)
    # def test_adding_new_recipe(self, appium_driver_setup, setup_appium_pages, mobile_data):
    #     logging.getLogger("root").info("Starting  test_remove_recipe_from_favorites")
    #     allure.attach('Starting  test_remove_recipe_from_favorites', attachment_type=allure.attachment_type.TEXT)
    #     appium_driver, big_oven_favoritePage, big_oven_new_recipe = setup_appium_pages
    #     big_oven_favoritePage.perform_sign_in(mobile_data["Email"], mobile_data["password"])
    #     assert big_oven_favoritePage.wait_for_logo_visibility(), "Logo is not visible after login"
    #     logging.getLogger("root").info("Login Successful")
    #     allure.attach('Login Successful', attachment_type=allure.attachment_type.TEXT)
    #     title = util.generate_rand_string(5)
    #     big_oven_new_recipe.adding_new_recipe(title, mobile_data["ingradients"], mobile_data["preparation"])
    #     logging.getLogger("root").info("New Recipe added successfully")
    #     allure.attach('New Recipe added successfully', attachment_type=allure.attachment_type.TEXT)
    #     assert big_oven_new_recipe.validate_added_recipe_title(
    #         title), f"Title does not match the provided title: {title}"
    #     big_oven_new_recipe.checkingThePresenceOfNewRecipe(title)
    #     logging.getLogger("root").info("Presence of newly added recipe ")
    #     allure.attach('Presence of newly added recipe ', attachment_type=allure.attachment_type.TEXT)
    #     big_oven_favoritePage.logout_from_big_oven()
    #     logging.getLogger("root").info("Ending test_adding_new_recipe")
    #     allure.attach('Ending test_adding_new_recipe', attachment_type=allure.attachment_type.TEXT)



