from selenium.webdriver.common.by import By


class ConfirmPage:
    def __init__(self, driver):
        self.driver = driver

    Xpath_to_select_country = (By.LINK_TEXT, "India")

    def selecting_country(self):
        return self.driver.find_element(*ConfirmPage.Xpath_to_select_country)

    Xpath_to_click_check_box = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    # driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()

    def check_box(self):
        return self.driver.find_element(*ConfirmPage.Xpath_to_click_check_box)

    Xpath_to_click_submit_btn = (By.XPATH, "//input[@type='submit']")

    # driver.find_element(By.XPATH, "//input[@type='submit']").click()

    def click_submit_button(self):
        return self.driver.find_element(*ConfirmPage.Xpath_to_click_submit_btn)

    # success_text = driver.find_element(By.CLASS_NAME, "alert-success").text

    Xpath_success_text = (By.CLASS_NAME, "alert-success")

    def get_success_text(self):
        return self.driver.find_element(*ConfirmPage.Xpath_success_text).text