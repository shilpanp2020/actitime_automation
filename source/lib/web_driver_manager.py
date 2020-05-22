from selenium import webdriver
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from source.lib import properties
from source.lib.listeners import MyListener


def start_browser(browser_name, url):
    web_driver = None

    if browser_name == "chrome":
        web_driver = webdriver.Chrome(
            executable_path=".\\resources\\drivers\\chromedriver")
    elif browser_name == "firefox":
        web_driver = webdriver.Firefox(
            executable_path=".\\resources\\drivers\\geckodriver")
    driver = EventFiringWebDriver(web_driver, MyListener())
    driver.implicitly_wait(properties.get_implicit_wait())
    driver.maximize_window()
    driver.get(url)

    return driver

