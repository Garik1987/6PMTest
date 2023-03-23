from selenium.webdriver.common.by import By
from Sources.BasePage.basePage import BasePage

class MainMenuPageLocator():
    mainMenuPageLocator = (By.XPATH, "//a[@href='/']")

class MainMenu(MainMenuPageLocator, BasePage):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def main_menu_page(self):
        mainMenuPage = self.find_element(*(self.mainMenuPageLocator))
        mainMenuPage.click()
