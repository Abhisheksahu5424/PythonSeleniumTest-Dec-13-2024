

from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    Xpath_Of_Shop_Button = (By.XPATH, "//a[text()='Shop']")

    def click_shop_tab(self):
        #  Click_ShopTab = driver.find_element(By.XPATH, "//a[text()='Shop']")
        return self.driver.find_element(*HomePage.Xpath_Of_Shop_Button)

    Xpath_Of_Name = (By.CSS_SELECTOR, "[name='name']")

    def enter_name(self):
        return self.driver.find_element(*HomePage.Xpath_Of_Name)

    Xpath_of_email = (By.NAME, "email")

    def enter_email(self):
        return self.driver.find_element(*HomePage.Xpath_of_email)

    Xpath_of_check_box = (By.ID, "exampleCheck1")

    def clicking_on_check_box(self):
        return self.driver.find_element(*HomePage.Xpath_of_check_box)

    Xpath_select_gender = (By.ID, "exampleFormControlSelect1")

    def select_gender(self):
        return self.driver.find_element(*HomePage.Xpath_select_gender)

    Xpath_of_submit_button = (By.XPATH, "//input[@value='Submit']")

    def click_submit_button(self):
        return self.driver.find_element(*HomePage.Xpath_of_submit_button)

    Xpath_form_submit_validation = (By.CSS_SELECTOR, "[class*='alert-success']")

    def form_submit_validation(self):
        return self.driver.find_element(*HomePage.Xpath_form_submit_validation)