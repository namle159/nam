from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Base:
    def __init__(self, driver):
        self.driver = driver

    def send_keys_to_element(self, locator, value):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        element.clear()
        element.send_keys(value)

    def click_element(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        element.click()

    def getElement(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        return element
    def getElements(self, locator):
        elements = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(locator))
        return elements
