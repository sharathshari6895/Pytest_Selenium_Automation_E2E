import os

import pytest
""" BaseTest class serves as the parent class for all test classes in UI_Test.
   It ensures that the 'init_driver' fixture is applied to all test methods inheriting from it. """


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    """This static method manages login and verifies the login outcome by comparing the current URL
     with the expected URL, using the provided login credentials and assertion data."""

    @staticmethod
    def login_and_assert(login_page, driver, login_data, assertion_data):
        login_page.click_login(login_data['userName'], login_data['PASSWORD'])
        assert driver.current_url == assertion_data['expected_url']

