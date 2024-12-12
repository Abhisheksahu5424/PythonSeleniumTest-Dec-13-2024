import time
from subprocess import check_output

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.CheckoutPage import CheckOutPage
from PageObjects.ConfirmPage import ConfirmPage
from PageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClassSetup
# If trying to run through terminal it was giving error so for that
# need to import path export PYTHONPATH="/home/abhishek/PythonSeleniumPOM_20-NOV-2024"



# @pytest.mark.usefixtures("setup")
class TestOne(BaseClassSetup):

    def test_e2e(self):
        driver = self.driver

        driver.implicitly_wait(6)
        home = HomePage(driver)
        home.click_shop_tab().click()

        # Click_ShopTab = driver.find_element(By.XPATH, "//a[text()='Shop']")
        # Click_ShopTab.click()
        # products_in_UI = driver.find_elements(By.CSS_SELECTOR, ".card.h-100")
        logs= self.get_logger()
        calling_class_check_out_page = CheckOutPage(driver)
        products_in_ui = calling_class_check_out_page.product_pages()
        logs.info("Getting All Products...!!!")
        for product in products_in_ui:
            product_name = product.find_element(By.XPATH, "div/h4/a").text
            logs.info(product_name)
            if product_name == "Blackberry":
                product.find_element(By.XPATH, "div/button").click()

        # checkout = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
        # checkout.click()
        calling_checkout_button = CheckOutPage(driver)
        checkout_button = calling_checkout_button.get_checkout_button()
        checkout_button.click()
        logs.info(checkout_button)
        # click_checkout = driver.find_element(By.XPATH, "//button[@class='btn btn-success']")
        # click_checkout.click()
        calling_checkout_button_for_clicking_checkout = CheckOutPage(driver)
        click_checkout_button = calling_checkout_button_for_clicking_checkout.clicking_checkout_page()
        click_checkout_button.click()

        # select_city = driver.find_element(By.ID, "country")
        # select_city.send_keys("Ind")
        calling_insert_country = CheckOutPage(driver)
        insert_country = calling_insert_country.insert_country()
        insert_country.send_keys("Ind")

        self.wait_till_locator_find_and_clicks("India")

        # driver.find_element(By.LINK_TEXT, "India").click()
        calling_select_country = ConfirmPage(driver)
        country = calling_select_country.selecting_country()
        country.click()

        # driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        calling_click_check_box = ConfirmPage(driver)
        check_box = calling_click_check_box.check_box()
        check_box.click()

        # driver.find_element(By.XPATH, "//input[@type='submit']").click()
        calling_submit_button = ConfirmPage(driver)
        submit_button = calling_submit_button.click_submit_button()
        submit_button.click()

        # success_text = driver.find_element(By.CLASS_NAME, "alert-success").text
        #
        # assert "Success! Thank you!" in success_text

        calling_get_success_text = ConfirmPage(driver)
        success_text = calling_get_success_text.get_success_text()
        assert "Success! Thank you!" in success_text, "Success message is not as expected!"