import pytest


def test_login_fails(login_page):
    login_page.open_login_page()
    login_page.lodin('user', 'password')
    assert login_page.get_error_message() == 'Неверный логин или пароль'


@pytest.fixture('username, password', [
    ('user', 'password'),
    ('user', 'password')
])
def test_login_success(login_page, username, password):
    login_page.open_login_page()
    login_page.login(username, password)
