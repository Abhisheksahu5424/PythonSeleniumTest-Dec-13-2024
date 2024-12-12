import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import logging
import inspect
@pytest.mark.usefixtures("setup")
class BaseClassSetup:

    def get_logger(self):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)  # Logger name needs to be change here.

        file_handler = logging.FileHandler("/home/abhishek/PythonSeleniumProject_13-dec-2024/utilities/logging.log", mode='w')  # File location

        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s : %(message)s")
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)  # FIleHandler Object
        logger.setLevel(logging.DEBUG)
        return logger

        # logger.debug("A debug statement is printed")
        # logger.info("Info statement")
        # logger.warning("Warning Statement")
        # logger.error("A major error came need to know that..!!!")
        # logger.critical("Something Happened critical..!!!")

    def wait_till_locator_find_and_clicks(self, text):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))