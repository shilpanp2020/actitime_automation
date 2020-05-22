from source.lib import excel_automation as excel
from source.lib import properties
from source.pages.home_page import HomePage
from source.pages.login_page import LoginPage
import pytest


class TestVersion:

    @pytest.mark.version
    @pytest.mark.regression
    def test_tc002_version_verify_product_version(self, request):
        # Collect all the test data required to test the feature
        username = properties.get_username()
        password = properties.get_password()
        expected_product_version = excel.get_data("actitime", "TC002", "ExpectedResult")

        # Create the object of pages classes
        login = LoginPage(request.node.driver)
        home = HomePage(request.node.driver)

        login.enter_user_name(username)
        login.enter_password(password)
        login.click_on_login_button()

        #home.click_on_question_icon()
        #home.click_on_about_actitime_link()
        #actual_product_version = home.get_product_version()

        #assert actual_product_version == expected_product_version, "actual product version {} is not matching with expected product version".format(actual_product_version, expected_product_version)
