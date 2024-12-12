import time

import pytest

from PageObjects.HomePage import HomePage
from TestData.HomePageData import HomePageData
from utilities.BaseClass import BaseClassSetup


class TestHomePage(BaseClassSetup):
    def test_form_submission(self, get_data):
        driver = self.driver

        logs = self.get_logger()
        calling_name = HomePage(driver)
        name = calling_name.enter_name()
        name.send_keys(get_data["First_Name"])
        logs.info("First Name is "+get_data["First_Name"])

        calling_email = HomePage(driver)
        email = calling_email.enter_email()
        email.send_keys(get_data["Email"])

        calling_check_box = HomePage(driver)
        checkbox = calling_check_box.clicking_on_check_box()
        checkbox.click()

        calling_gender = HomePage(driver)
        gender = calling_gender.select_gender()
        gender.click()

        calling_submit_button = HomePage(driver)
        submit_button = calling_submit_button.click_submit_button()
        submit_button.click()

        calling_form_validation = HomePage(driver)
        from_validation = calling_form_validation.form_submit_validation().text
        assert "Success! The Form has been submitted successfully!." in from_validation
        time.sleep(5)

        self.driver.refresh()

    @pytest.fixture(params=HomePageData.test_home_page_data)
    def get_data(self, request):
        return request.param
