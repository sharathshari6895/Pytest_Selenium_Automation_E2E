# from Tests.UI_Test.BaseTest import BaseTest
# from Tests.configtest import init_driver, assertion_data, ui_data, logger_setup,setup_pages
# import allure, logging, pytest
#
#
# class TestCart(BaseTest):
#
#     # Test scenario for logging into the application with valid credentials, selecting a product,
#     # adding it to the cart, and verifying if the product is added to the cart
#     @pytest.mark.run(order=3)
#     @allure.severity(allure.severity_level.CRITICAL)
#     @pytest.mark.parametrize("browser", ["chrome"])
#     def test_add_to_cart(self, setup_pages, ui_data, assertion_data, logger_setup,browser):
#         logging.getLogger("root").info("Starting test_add_to_cart")
#         allure.attach('Starting test_add_to_cart', attachment_type=allure.attachment_type.TEXT)
#         driver, login_page, cart_page, _ = setup_pages
#         logging.getLogger("root").info("Login successfully")
#         allure.attach('Login successfully', attachment_type=allure.attachment_type.TEXT)
#         self.login_and_assert(login_page, driver, ui_data, assertion_data)
#         cart_page.select_product()
#         assert cart_page.wait_for_product_element(), "Product 'Sauce Labs Backpack' is not present"
#         cart_page.add_to_cart()
#         logging.getLogger("root").info("Adding Product to the cart")
#         allure.attach('Adding Product to the cart', attachment_type=allure.attachment_type.TEXT)
#         cart_page.click_cart_icon()
#         logging.getLogger("root").info("Checking Product in the cart")
#         allure.attach('Checking Product in the cart', attachment_type=allure.attachment_type.TEXT)
#         cart_page.checking_productIn_cart(assertion_data["product_name"])
#         cart_page.logout_page()
#         logging.getLogger("root").info("Ending test_add_to_cart")
#         allure.attach('Ending test_add_to_cart', attachment_type=allure.attachment_type.TEXT)
#
#     # Test scenario for logging into the application with valid credentials, navigating to the cart,
#     # removing a product from the cart, and verifying if the product is removed from the cart
#     @pytest.mark.run(order=4)
#     @allure.severity(allure.severity_level.CRITICAL)
#     @pytest.mark.parametrize("browser", ["chrome"])
#     def test_remove_from_cart(self, setup_pages, ui_data, assertion_data, logger_setup,browser):
#         driver, login_page, cart_page, _ = setup_pages
#         self.login_and_assert(login_page, driver, ui_data, assertion_data)
#         logging.getLogger("root").info("Starting test_remove_from_cart")
#         allure.attach('Starting test_remove_from_cart', attachment_type=allure.attachment_type.TEXT)
#         cart_page.select_product()
#         cart_page.add_to_cart()
#         logging.getLogger("root").info("Product added to the cart successfully")
#         allure.attach('Product added to the cart successfully', attachment_type=allure.attachment_type.TEXT)
#         assert not cart_page.is_shopping_cart_empty(), "Shopping cart is empty"  # Assert shopping cart is not empty before removing
#         cart_page.remove_item_from_cart(assertion_data["product_name"])
#         logging.getLogger("root").info("Product is removed from the cart successfully")
#         allure.attach('Product is removed from the cart successfully', attachment_type=allure.attachment_type.TEXT)
#         assert cart_page.is_shopping_cart_empty(), "Product still present in cart after removal"  # Assert product is removed from cart
#         logging.getLogger("root").info("Ending test_remove_from_cart")
#         allure.attach('Ending test_remove_from_cart', attachment_type=allure.attachment_type.TEXT)
