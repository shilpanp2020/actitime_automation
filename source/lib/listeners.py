from selenium.webdriver.support.abstract_event_listener import AbstractEventListener
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from source.lib import properties
from source.lib import helper


class MyListener(AbstractEventListener):

    def before_find(self, by, value, driver):
        helper.wait_for_ajax_to_complete(driver)

    def before_click(self, element, driver):
        wait = WebDriverWait(driver, properties.get_explicit_wait())
        wait.until(ec.visibility_of(element))

    def on_exception(self, exception, driver):
        helper.take_screen_shot_and_attach(driver, exception)
        driver.quit()
