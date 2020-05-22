from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.set_page_load_timeout(15)
        self.wait = WebDriverWait(self.driver, 15)

    def find_element(self, locator, value):
        try:
            web_element = self.driver.find_element(locator, value)
            return web_element
        except NoSuchElementException:
            print("Web element is not available in the DOM")

    def wait_for_element_to_be_visible(self, web_element):
        try:
            self.wait.until(ec.visibility_of(web_element))
        except TimeoutException:
            print("Web element is not visible in the Application UI")

