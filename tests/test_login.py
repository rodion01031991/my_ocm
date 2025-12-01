import pytest
import allure

@allure.feature("Авторизация")
@allure.title("Авторизаиця с недействительными учетными данными")
@allure.severity(allure.severity_level.CRITICAL)
def test_login_fail(login_page):
    with allure.step('Открыть страницу авторизации'):
        login_page.open_login_page()
    with allure.step('Ввести в форму авторизации недействительные учетные данные'):
         login_page.login('user', 'password')
    with allure.step('Отображается ошибка - Неверный логин или пароль'):
        assert login_page.get_error_message() == 'Неверный логин или пароль'


@pytest.mark.parametrize('username, password', [
    ('ger@fgdgf.ftg', '123456'),
    ('+7 (907) 645-21-31', '123456')
])
@allure.feature("Авторизация")
@allure.title("Авторизаиця с корректными учетными данными")
@allure.severity(allure.severity_level.CRITICAL)
def test_login_success(login_page, username, password):
    with allure.step('Открыть страницу авторизации'):
        login_page.open_login_page()
    with allure.step('Ввести в форму авторизации корректные учетные данные'):
        login_page.login(username, password)
    with allure.step('Url изменился'):
        login_page.page.wait_for_url("https://rc.dev.oneclickmoney.ru/account/")