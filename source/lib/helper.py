import allure


def wait_for_ajax_to_complete(driver):
    driver.execute_script("var callback = arguments[arguments.length - 1];" +
    "var xhr = new XMLHttpRequest();" + "xhr.open('GET', '/Ajax_call', true);" +
    "xhr.onreadystatechange = function() {" + "  if (xhr.readyState == 4) {" +
    "callback(xhr.responseText);" + "  }" + "};" + "xhr.send();")


def take_screen_shot_and_attach(driver, file_name):
    allure.attach(driver.get_screenshot_as_png(),
                  name=file_name,
                  attachment_type=allure.attachment_type.PNG)
