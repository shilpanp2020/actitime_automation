from selenium.webdriver.common.by import By
from source.pages.base_page import BasePage
import allure


class LoginPage(BasePage):

    def __username_tb(self): return self.find_element(By.ID, "username")
    def __password_tb(self): return self.find_element(By.NAME, "pwd")
    def __login_button(self): return self.find_element(By.ID, "loginButton")

    @allure.step
    def enter_user_name(self, user):
        self.__username_tb().send_keys(user)

    @allure.step
    def enter_password(self, password):
        self.__password_tb().send_keys(password)

    @allure.step
    def click_on_login_button(self):
        self.__login_button().click()

    @allure.step
    def get_title(self):
        return self.driver.title
