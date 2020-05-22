import pytest

allure_results_path = ".//resources//reports//allure-results"
commands = ['-n', '2', "--alluredir", allure_results_path]

pytest.main(commands)
