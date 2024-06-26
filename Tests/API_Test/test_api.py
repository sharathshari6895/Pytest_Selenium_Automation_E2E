# import pytest
# import requests
# from Tests.configtest import api_data_fixture, auth_token, created_booking_id, api_config_from_ini, logger_setup
# import logging
# import allure


# @pytest.mark.usefixtures("created_booking_id", "auth_token", "api_config_from_ini", "api_data_fixture", "logger_setup")
# class TestAPITest:
#     """Test method to retrieve all booking details.
#            It sends a GET request to the API endpoint for bookings,
#            verifies that the response status code is 200,
#            and checks if at least one bookingid is present in the response data. """

#     @pytest.mark.run(order=7)
#     @pytest.mark.timeout(1000)
#     @allure.severity(allure.severity_level.NORMAL)
#     def test_get_all_bookings(self, api_data_fixture, auth_token, api_config_from_ini):
#         allure.attach('Starting test_get_all_bookings', attachment_type=allure.attachment_type.TEXT)
#         logging.info("Starting test_get_all_bookings")
#         api_config = api_config_from_ini
#         allure.attach('Fetching bookings from API', attachment_type=allure.attachment_type.TEXT)
#         logging.debug("Fetching bookings from API")
#         response = requests.get(api_config['api_url'] + api_config['booking_base_end_point'],
#                                 headers={'Cookie': 'token=' + auth_token})
#         assert response.status_code == 200, f"Failed to get all bookings. Status code: {response.status_code}"
#         data = response.json()
#         assert any("bookingid" in item for item in data), "No bookings found"
#         allure.attach('Bookings fetched successfully', attachment_type=allure.attachment_type.TEXT)
#         logging.info("Bookings fetched successfully")
#         allure.attach('Ending test_get_all_bookings', attachment_type=allure.attachment_type.TEXT)
#         logging.info("Ending test_get_all_bookings")
# #
#     """
#         Test method to create a new booking.
#         It sends a POST request with booking data to the API endpoint,
#         verifies that the response status code is 200,
#         retrieves the created booking for validation,
#         and checks if the created booking data matches the sent data.
#         """

#     @pytest.mark.run(order=8)
#     @pytest.mark.timeout(1000)
#     @allure.severity(allure.severity_level.NORMAL)
#     def test_create_booking(self, api_data_fixture, auth_token, api_config_from_ini):
#         allure.attach('Starting test_create_booking', attachment_type=allure.attachment_type.TEXT);
#         logging.info("Starting test_create_booking")
#         assert auth_token is not None, "Authentication token not obtained"
#         api_config = api_config_from_ini
#         allure.attach('Sending request to create a booking', attachment_type=allure.attachment_type.TEXT)
#         logging.debug("Sending request to create a booking")
#         response = requests.post(api_config['api_url'] + api_config['booking_base_end_point'],
#                                  json=api_data_fixture.get("booking_data", {}),
#                                  headers={'Cookie': 'token=' + auth_token})
#         assert response.status_code == 200, f"Failed to create booking. Status code: {response.status_code}"
#         booking_id = response.json().get("bookingid", '')
#         allure.attach('Retrieving created booking for validation', attachment_type=allure.attachment_type.TEXT);
#         logging.debug("Retrieving created booking for validation")
#         response = requests.get(
#             api_config['api_url'] + '/' + api_config['booking_detail_end_point'].format(bookingid=booking_id))
#         assert response.status_code == 200, f"Failed to retrieve created booking. Status code: {response.status_code}"
#         assert response.json() == api_data_fixture.get("booking_data", {}), "Created booking data does not match"
#         allure.attach('Ending test_create_booking', attachment_type=allure.attachment_type.TEXT)
#         logging.info("Ending test_create_booking")

#     """Test method to update booking details.
#     It sends a PUT request with updated booking data to the API endpoint,
#     verifies that the response status code is 200,
#     and checks if the first name and last name are updated correctly. """

#     @pytest.mark.run(order=9)
#     @pytest.mark.timeout(1000)
#     @allure.severity(allure.severity_level.CRITICAL)
#     def test_update_booking(self, api_data_fixture, auth_token, created_booking_id, api_config_from_ini):
#         allure.attach('Starting test_update_booking', attachment_type=allure.attachment_type.TEXT)
#         logging.info("Starting test_update_booking")
#         assert auth_token is not None, "Authentication token not obtained"
#         assert created_booking_id is not None, "Created booking ID is None"
#         api_config = api_config_from_ini
#         updated_data = api_data_fixture.get("updated_booking_data", {})
#         allure.attach('Preparing data for updating booking', attachment_type=allure.attachment_type.TEXT)
#         logging.debug("Preparing data for updating booking")
#         response = requests.put(
#             api_config['api_url'] + '/' + api_config['booking_detail_end_point'].format(bookingid=created_booking_id),
#             json=updated_data, headers={'Cookie': 'token=' + auth_token})
#         allure.attach('Sending request to update booking', attachment_type=allure.attachment_type.TEXT);
#         logging.debug("Sending request to update booking")
#         assert response.status_code == 200, f"Failed to update booking. Status code: {response.status_code}"
#         assert response.json().get("firstname") == updated_data.get("firstname"), "First name not updated"
#         assert response.json().get("lastname") == updated_data.get("lastname"), "Last name not updated"
#         allure.attach('Booking updated successfully', attachment_type=allure.attachment_type.TEXT);
#         logging.info("Booking updated successfully")
#         allure.attach('Ending test_update_booking', attachment_type=allure.attachment_type.TEXT);
#         logging.info("Ending test_update_booking")

#     """Test method to patch booking details.
#     It sends a PATCH request with patch data to the API endpoint,
#          verifies that the response status code is 200. """

#     @pytest.mark.run(order=10)
#     @pytest.mark.timeout(1000)
#     @allure.severity(allure.severity_level.CRITICAL)
#     def test_patch_booking(self, api_data_fixture, auth_token, created_booking_id, api_config_from_ini):
#         allure.attach('Starting test_patch_booking', attachment_type=allure.attachment_type.TEXT)
#         logging.info("Starting test_patch_booking")
#         assert api_data_fixture is not None, "API data fixture is None"
#         assert auth_token is not None, "Authentication token not obtained"
#         assert created_booking_id is not None, "Created booking ID is None"
#         patch_data = api_data_fixture.get("patch_data", {})
#         api_config = api_config_from_ini
#         allure.attach('Sending request to patch booking', attachment_type=allure.attachment_type.TEXT);
#         logging.debug("Sending request to patch booking")
#         response = requests.patch(
#             api_config['api_url'] + api_config['booking_base_end_point'] + '/' + str(created_booking_id),
#             json=patch_data, headers={'Cookie': 'token=' + auth_token})
#         assert response.status_code == 200, f"Failed to patch booking. Status code: {response.status_code}"
#         allure.attach('Booking patched successfully', attachment_type=allure.attachment_type.TEXT);
#         logging.info("Booking patched successfully")

#     """Test method to delete a booking.
#     It sends a DELETE request to the API endpoint for the specific booking,
#            verifies that the response status code is 201. """

#     @pytest.mark.run(order=11)
#     @pytest.mark.timeout(1000)
#     @allure.severity(allure.severity_level.CRITICAL)
#     def test_delete_booking(self, api_data_fixture, auth_token, created_booking_id, api_config_from_ini):
#         allure.attach('Starting test_delete_booking', attachment_type=allure.attachment_type.TEXT)
#         logging.info("Starting test_delete_booking")
#         assert api_data_fixture is not None, "API data fixture is None"
#         assert auth_token is not None, "Authentication token not obtained"
#         assert created_booking_id is not None, "Created booking ID is None"
#         api_config = api_config_from_ini
#         allure.attach('Sending request to delete booking', attachment_type=allure.attachment_type.TEXT);
#         logging.debug("Sending request to delete booking")
#         response = requests.delete(api_config.get('api_url', '') + '/' + api_config['booking_detail_end_point'].format(
#             bookingid=created_booking_id),
#                                    headers={'Cookie': 'token=' + auth_token, 'Content-Type': 'application/json'})
#         assert response.status_code == 201, f"Failed to delete booking. Status code: {response.status_code}"
#         logging.info("Booking deleted successfully")
#         allure.attach('Booking deleted successfully', attachment_type=allure.attachment_type.TEXT)
