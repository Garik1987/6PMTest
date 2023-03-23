from selenium.webdriver.common.by import By
from Sources.BasePage.basePage import BasePage

class MenProductLocators():
    clickMenProductLocators = (By.XPATH, "(//span[@class='dE-z'])[2]")

class MyFirstProductLocators():
    clickMyFirstProductLocators = (By.XPATH, "//a[@data-style-id='5811252']")

class MenProduct(MenProductLocators, BasePage):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def click_men_product(self):
        menProductElement = self.find_element(*(self.clickMenProductLocators))
        menProductElement.click()

class MyFirstProduct(MyFirstProductLocators, BasePage):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def click_my_first_product(self):
        myFirstProductElement = self.find_element(*(self.clickMyFirstProductLocators))
        myFirstProductElement.click()
