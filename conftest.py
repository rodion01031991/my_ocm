import pytest
@pytest.fixture
def login_page(page):
    from pages.login_page import LoginPage
    return LoginPage(page)

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {"width": 1920, "height": 1080},
        "ignore_https_errors": True,
    }

@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    return {
        **browser_type_launch_args,
        "headless": False,
        "slow_mo": 1000,
    }

@pytest.fixture()
def first_step_of_registration_page(page):
    from pages.first_step_of_registration_page import FirstStepOfRegistrationPage
    return FirstStepOfRegistrationPage(page)

@pytest.fixture()
def third_step_of_registration_page(page):
    from pages.third_step_of_registration_page import ThirdStepOfRegistrationPage
    return ThirdStepOfRegistrationPage(page)

@pytest.fixture()
def common_functions_page(page):
    from pages.common_functions_page import CommonFunctionsPage
    return CommonFunctionsPage(page)