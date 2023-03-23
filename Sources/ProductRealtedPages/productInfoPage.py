from selenium.webdriver.common.by import By
from Sources.BasePage.basePage import BasePage

class ProductInfoPageLocators():
    addToShoppingBagLocators = (By.XPATH, '//button[@data-track-value="Add-To-Cart"]')
    addToSyzeLocators = (By.XPATH, '//*[@for="radio-2841-9593349"]')

class ProductInfo(ProductInfoPageLocators, BasePage):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def click_add_to_syze_button(self):
        addToSyzeButtonElement = self.find_element(*(self.addToShoppingBagLocators))
        addToSyzeButtonElement.click()

    def click_add_to_shopping_bag_button(self):
        addToShoppingBadelement = self.find_element(*(self.addToShoppingBagLocators))
        addToShoppingBadelement.click()

