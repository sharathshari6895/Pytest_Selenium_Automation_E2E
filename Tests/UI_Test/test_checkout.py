# import pytest
# from Tests.UI_Test.BaseTest import BaseTest
# from Tests.configtest import init_driver, assertion_data, ui_data, logger_setup,setup_pages
# import allure, logging
#
#
# class TestCheckout(BaseTest):
#
#     # Test scenario for logging into the application with valid credentials, navigating to the cart,
#     # clicking on checkout, filling the user details, verifying the details are correct, and clicking on finish
#     @pytest.mark.run(order=5)
#     @pytest.mark.parametrize("browser", ["chrome"])
#     @allure.severity(allure.severity_level.CRITICAL)
#     def test_checkout(self, setup_pages, ui_data, assertion_data, logger_setup,browser):
#         logging.getLogger("root").info("Starting test_checkout")
#         allure.attach('Starting test_checkout', attachment_type=allure.attachment_type.TEXT)
#         driver, login_page, cart_page, checkout_page = setup_pages
#         self.login_and_assert(login_page, driver, ui_data, assertion_data)
#         cart_page.add_product_to_cart()
#         assert checkout_page.is_checkout_text_visible(), "Checkout text is not visible"
#         checkout_page.click_checkout()
#         logging.getLogger("root").info("Adding user details for checkout")
#         allure.attach('Adding user details for checkout', attachment_type=allure.attachment_type.TEXT)
#         checkout_page.checkout_details(ui_data['firstName'], ui_data['lastName'], ui_data['Zipcode'])
#         checkout_page.continue_checkout()
#         checkout_page.finish_checkout()
#         assert checkout_page.is_thank_you_message_visible(), "Thank you message is not visible"
#         logging.getLogger("root").info("Checkout Successful")
#         allure.attach('Checkout Successful', attachment_type=allure.attachment_type.TEXT)
#
#     # Test scenario for logging into the application with valid credentials, clicking on the sorting dropdown,
#     # selecting 'Price: Low to High' option, and verifying if it is applied
#     @pytest.mark.run(order=6)
#     @allure.severity(allure.severity_level.NORMAL)
#     @pytest.mark.parametrize("browser", ["chrome"])
#     def test_sort_products(self, setup_pages, ui_data, assertion_data, logger_setup,browser):
#         logging.getLogger("root").info("Starting test_sort_products")
#         allure.attach('Starting test_sort_products', attachment_type=allure.attachment_type.TEXT)
#         driver, login_page, _, checkout_page = setup_pages
#         self.login_and_assert(login_page, driver, ui_data, assertion_data)
#         assert checkout_page.is_dropdown_visible(), "Dropdown element is not visible"
#         checkout_page.select_dropdown()
#         checkout_page.compare_product_prices()
#         logging.getLogger("root").info("Products sorted successfully")
#         allure.attach('Products sorted successfully', attachment_type=allure.attachment_type.TEXT)
#         logging.getLogger("root").info("Ending test_sort_products")
#         allure.attach('Ending test_sort_products', attachment_type=allure.attachment_type.TEXT)
