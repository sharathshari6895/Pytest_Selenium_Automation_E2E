# import pytest
# from Tests.UI_Test.BaseTest import BaseTest
# from Tests.configtest import init_driver, ui_data, assertion_data
# import allure
# from Tests.configtest import logger_setup, setup_pages
# import logging
# from selenium import webdriver


# class TestLogin(BaseTest):

#     # Test scenario for logging into the application with valid credentials

#     @pytest.mark.run(order=2)
#     @pytest.mark.parametrize("browser", ["chrome"])
#     def test_valid_sign_in(self, setup_pages, ui_data, assertion_data, logger_setup, request, init_driver, browser):
#         logging.getLogger("root").info("Starting test_valid_signin")
#         allure.attach('Starting test_valid_signin', attachment_type=allure.attachment_type.TEXT)
#         driver, login_page, _, _ = setup_pages
#         logging.getLogger("root").info("Logging with valid credentials")
#         allure.attach('Logging with valid credentials', attachment_type=allure.attachment_type.TEXT)
#         self.login_and_assert(login_page, driver, ui_data, assertion_data)
#         allure.attach('Logging successfully', attachment_type=allure.attachment_type.TEXT)
#         logging.getLogger("root").info("Ending test_valid_signin")



#     @pytest.mark.run(order=2)
#     @pytest.mark.parametrize("browser", ["chrome"])
#     @allure.severity(allure.severity_level.NORMAL)
#     def test_invalid_sign_in(self, setup_pages, ui_data, assertion_data, init_driver, logger_setup, browser):
#         logging.getLogger("root").info("Starting test_invalid_signin")
#         allure.attach('Starting test_invalid_signin', attachment_type=allure.attachment_type.TEXT)
#         driver, login_page, _, _ = setup_pages
#         login_page.click_login(ui_data['userName'], ui_data['INVALID PASSWORD'])
#         expected_url = assertion_data.get('expected_url')
#         if expected_url is not None:
#             assert driver.current_url == expected_url
#         else:
#             raise KeyError("Key 'expected_url' not found in assertion_data")
#         logging.getLogger("root").info("Ending test_invalid_signin")
#         allure.attach('Ending test_invalid_signin', attachment_type=allure.attachment_type.TEXT)
