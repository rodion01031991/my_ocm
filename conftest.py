import pytest
from pages.login_page import LoginPage

@pytest.fixture
def login_page(page):
    return LoginPage(page)

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {"width": 1200, "height": 800},
        "ignore_https_errors": True,
    }

@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    return {
        **browser_type_launch_args,
        "headless": False,
        "slow_mo": 1000,
    }