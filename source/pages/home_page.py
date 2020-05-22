from selenium.webdriver.common.by import By
from source.pages.base_page import BasePage
import allure


class HomePage(BasePage):

    def __question_icon(self): return self.find_element(By.XPATH, "(//div[@class='menu_icon'])[3]")
    def __log_out_link(self): return self.find_element(By.ID, "logoutLink")
    def __about_actitime_link(self): return self.find_element(By.XPATH, "//a[text()='About your actiTIME']")
    def __product_version(self): return self.find_element(By.CSS_SELECTOR, "span.productVersion")

    @allure.step
    def click_on_question_icon(self):
        self.__question_icon().click()

    @allure.step
    def click_on_about_actitime_link(self):
        self.__about_actitime_link().click()

    @allure.step
    def get_product_version(self):
        return self.__product_version().text

    def click_on_log_out(self):
        self.__log_out_link().click()
