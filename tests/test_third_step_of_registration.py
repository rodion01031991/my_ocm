import pytest
import allure
from playwright.sync_api import Page, expect
from pages.third_step_of_registration_page import ThirdStepOfRegistrationPage
from pages.common_functions_page import CommonFunctionsPage

@allure.epic("Веб-приложение OCM")
@allure.feature("Регистрация пользователя")
@allure.story("Проверка валидации третьей страницы регистрации")
@allure.title("Проверка чекбокса 'Официально не трудоустроен'")
@allure.severity(allure.severity_level.NORMAL)
def test_checkbox_Not_officially_employed(page: Page):
    third_step_of_registration_page = ThirdStepOfRegistrationPage(page)
    common_functions_page = CommonFunctionsPage(page)
    with allure.step('Вызываем функцию по заполению 1 шага регистрации и перехда на 2 шаг регистрации'):
        common_functions_page.moving_to_the_second_step(page)
    with allure.step('Вызываем функцию по заполению 2 шага регистрации и перехда на 3 шаг регистрации'):
        common_functions_page.moving_from_the_second_step_to_the_third_step(page)
    with allure.step('Проставляем чекбокс'):
        third_step_of_registration_page.check_checkbox_is_workless()
    with allure.step('Проверяем поля "Место работы" "Адрес места работы" "Рабочий телефон" не отображаются'):
        third_step_of_registration_page.verify_input_not_visible()
    with allure.step('Снимаем чекбокс'):
        third_step_of_registration_page.uncheck_checkbox_is_workless()
    with allure.step('Проверяем поля "Место работы" "Адрес места работы" "Рабочий телефон" отображаются'):
        third_step_of_registration_page.verify_input_visible()

@allure.epic("Веб-приложение OCM")
@allure.feature("Регистрация пользователя")
@allure.story("Проверка валидации третьей страницы регистрации")
@allure.title("Проверка наличие чекбоксов на 3 шаге регистрации")
@allure.severity(allure.severity_level.NORMAL)
def test_checking_the_checkboxes_third_registration_step(page: Page):
    third_step_of_registration_page = ThirdStepOfRegistrationPage(page)
    common_functions_page = CommonFunctionsPage(page)
    with allure.step('Вызываем функцию по заполению 1 шага регистрации и перехда на 2 шаг регистрации'):
        common_functions_page.moving_to_the_second_step(page)
    with allure.step('Вызываем функцию по заполению 2 шага регистрации и перехда на 3 шаг регистрации'):
        common_functions_page.moving_from_the_second_step_to_the_third_step(page)
    with allure.step('Жмем кнопку "следующим"'):
        third_step_of_registration_page.click_next_button()
    with allure.step('Проверяем наличие чекбоксов'):
        third_step_of_registration_page.checking_the_checkboxes_third_registration_step()

@allure.epic("Веб-приложение OCM")
@allure.feature("Регистрация пользователя")
@allure.story("Проверка валидации третьей страницы регистрации")
@allure.title("Проверка поля 'Место работы'")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize(
    "value, expected_error",
    [
        ("Рога", None),
        ("Roga", None),
        ("123", None),
        ("!@:#&", None),
        ("", "Необходимо заполнить «Место работы»."),
    ]
)
def test_place_of_work_input(page: Page, value: str, expected_error: str):
    third_step_of_registration_page = ThirdStepOfRegistrationPage(page)
    common_functions_page = CommonFunctionsPage(page)
    with allure.step('Вызываем функцию по заполению 1 шага регистрации и перехда на 2 шаг регистрации'):
         common_functions_page.moving_to_the_second_step(page)
    with allure.step('Вызываем функцию по заполению 2 шага регистрации и перехда на 3 шаг регистрации'):
         common_functions_page.moving_from_the_second_step_to_the_third_step(page)
    with allure.step(f"Ввод значения в поле «Место работы»: '{value}'"):
        third_step_of_registration_page.place_of_work_input.fill(value)
        third_step_of_registration_page.place_of_work_input.blur()
    with allure.step(f"Проверка: отображается ошибка '{expected_error}'"):
        if expected_error is None:
            expect(third_step_of_registration_page.error_message_necessary_fill_place_of_work).not_to_be_visible()
        else:
            expect(third_step_of_registration_page.error_message_necessary_fill_place_of_work).to_be_visible()
            actual_error = third_step_of_registration_page.error_message_necessary_fill_place_of_work.text_content()
            assert expected_error in actual_error, f'Ожидалось: "{expected_error}", отображается: "{actual_error}"'







