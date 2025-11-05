import pytest


def test_login_fail(login_page):
    login_page.open_login_page()
    login_page.login('user', 'password')
    assert login_page.get_error_message() == 'Неверный логин или пароль'


@pytest.mark.parametrize('username, password', [
    ('user', 'password'),
    ('user', 'password')
])
def test_login_success(login_page, username, password):
    login_page.open_login_page()
    login_page.login(username, password)
