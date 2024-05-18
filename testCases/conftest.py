import pytest_html
from selenium import webdriver
import pytest
from _pytest.config import exceptions
from _pytest.reports import TestReport


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Chrome Browser is Launched Successfully")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Firefox Browser is Launched Successfully")
    else:
        driver = webdriver.Chrome()
        # driver = webdriver.Ie() # Means Internet Explorar what browser you are using as a default browser # I dont have the setup of internet explorar theats why using the chrome Browser

    return driver


def pytest_addoption(parser):  # This will get the value from CLI hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return the browser value to setup method
    return request.config.getoption("--browser")


# Suppose if we didnt pass any browser it gives error "UnboundLocalErroe we need to handel this
# so we need to pass some default browser if we dont pass any name"


################################## To  generate HTML Report I need to write sommething code (Pytest HTML Report)######################################

# Its a hook for adding HTML Report to the environment

def pytest_configure(config):
    config.option.metadata = {
        'Project Name': 'Your_Project_Name',
        'Module Name': 'Your_Module_Name',
        'Environment': 'Production'
    }


# Its a hook for delete / Modify environment info too HTML Report
# @pytest.mark.optionalhook
# # To remove the information the default values in the HTML Report
# def pytest_metadata(metadata):
#     metadata.pop("JAVA HOME", None)
#     metadata.pop("Plugins", None)

# html_file_path = '/Users/pranjalnama/PycharmProjects/nopcommereApp/Reports/report.html'
# new_text = '<p>This is the new text to be added.</p>'


# @pytest.fixture(scope="session", autouse=True)
# def test_add_text_to_html():
#     print("Cleanup after test case")
#
#     # Read the contents of the HTML file
#     with open(html_file_path, 'r') as file:
#         html_content = file.read()
#
#     # Modify the HTML content to add the new text
#     modified_html_content = html_content + '\n' + new_text
#
#     # Write the modified content back to the HTML file
#     with open(html_file_path, 'w') as file:
#         file.write(modified_html_content)
