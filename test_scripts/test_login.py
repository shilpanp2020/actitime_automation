from source.lib import  excel_automation as excel
from source.pages.login_page import LoginPage
import pytest


class TestLogin:

    @pytest.mark.smoke
    @pytest.mark.login
    def test_tc001_login_invalid_login_test(self, request):
        # Collect all the test data required to test the feature
        invalid_user = excel.get_data("actitime", "TC001", "InvalidUser")
        invalid_pass = excel.get_data("actitime", "TC001", "InvalidPass")
        expected_result = excel.get_data("actitime", "TC001", "ExpectedResult")

        # Create the object of pages classes
        login = LoginPage(request.node.driver)

        login.enter_user_name(invalid_user)
        login.enter_password(invalid_pass)
        login.click_on_login_button()

        actual_result = login.get_title()

        assert expected_result in actual_result, "{} is not matching with {}".format(actual_result, expected_result)

