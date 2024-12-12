from selenium.webdriver.common.by import By


class CheckOutPage:
    def __init__(self, driver):
        self.driver=driver

    Xpath_Of_All_Products_present = (By.CSS_SELECTOR, ".card.h-100")
    # products_in_UI = driver.find_elements(By.CSS_SELECTOR, ".card.h-100")
    def product_pages(self):
        return self.driver.find_elements(*CheckOutPage.Xpath_Of_All_Products_present)


    Xpath_of_Checkout_Button = (By.CSS_SELECTOR, ".btn-primary")
    # driver.find_element(By.CSS_SELECTOR, ".btn-primary")

    def get_checkout_button(self):
        return self.driver.find_element(*CheckOutPage.Xpath_of_Checkout_Button)

    Xpath_Of_click_checkout_button = (By.XPATH, "//button[@class='btn btn-success']")

    # driver.find_element(By.XPATH, "//button[@class='btn btn-success']")

    def clicking_checkout_page(self):
        return self.driver.find_element(*CheckOutPage.Xpath_Of_click_checkout_button)

    Xpath_to_insert_country = (By.ID, "country")
    # select_city = driver.find_element(By.ID, "country")

    def insert_country(self):
        return self.driver.find_element(*CheckOutPage.Xpath_to_insert_country)