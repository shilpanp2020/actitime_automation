import pytest
from source.lib.web_driver_manager import start_browser
from source.lib import properties


def get_browser():
    prop_values = properties.get_browser()
    browser_names = prop_values.split(',')
    browsers = []
    for browser in browser_names:
        browsers.append(browser)
    return browsers


@pytest.fixture(scope="function",
                autouse=True,
                params=get_browser())
def set_up_functions(request):
    browser = request.param
    url = properties.get_url()
    driver = start_browser(browser, url)

    if request is not None:
        request.node.driver = driver

    yield
    driver.quit()

