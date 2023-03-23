import time
from selenium import webdriver
import unittest
from Sources.NavigationBar.navigationBar import NavigationBar
from Sources.ProductRealtedPages.searchResultPage import MenProduct
from Sources.ProductRealtedPages.searchResultPage import MyFirstProduct
from Sources.ProductRealtedPages.productInfoPage import ProductInfo
from Sources.MainMenuPage.mainMenuPage import MainMenu

class MyTest (unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.delete_all_cookies()
        self.driver.maximize_window()
        self.driver.get("https://www.6pm.com/")
        self.searchButtonObj = NavigationBar(self.driver)
        self.menProductObj = MenProduct(self.driver)
        self.myFirstProductObj = MyFirstProduct(self.driver)
        self.addToShoppingBagObj = ProductInfo(self.driver)
        self.addToSyzeButtonObj = ProductInfo(self.driver)
        self.mainMenuPage = MainMenu(self.driver)

    def test_6PM(self):
        self.searchButtonObj.fill_search_fild("adidas ultraboost")
        self.searchButtonObj.click_search_button_element()
        self.menProductObj.click_men_product()
        self.myFirstProductObj.click_my_first_product()
        self.addToSyzeButtonObj.click_add_to_syze_button()
        self.addToShoppingBagObj.click_add_to_shopping_bag_button()
        time.sleep(5)
        self.mainMenuPage.main_menu_page()
        time.sleep(5)

    def tearDown(self) -> None:
        self.driver.close()

