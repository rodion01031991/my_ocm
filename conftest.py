import pytest
from pages.login_page import LoginPage
from pages.first_step_of_registration_page import FirstStepOfRegistrationPage

@pytest.fixture
def login_page(page):
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
    return FirstStepOfRegistrationPage(page)