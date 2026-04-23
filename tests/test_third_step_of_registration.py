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

@allure.epic("Веб-приложение OCM")
@allure.feature("Регистрация пользователя")
@allure.story("Проверка валидации третьей страницы регистрации")
@allure.title("Проверка поля 'Адрес места работы'")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize(
    "value, expected_error",
    [
        ("Нарния", None),
        ("Narnia", None),
        ("654", None),
        ("#^$&№", None),
        ("", "Необходимо заполнить «Адрес места работы»."),
    ]
)
def test_workplace_address_input(page: Page, value: str, expected_error: str):
    third_step_of_registration_page = ThirdStepOfRegistrationPage(page)
    common_functions_page = CommonFunctionsPage(page)
    with allure.step('Вызываем функцию по заполению 1 шага регистрации и перехда на 2 шаг регистрации'):
         common_functions_page.moving_to_the_second_step(page)
    with allure.step('Вызываем функцию по заполению 2 шага регистрации и перехда на 3 шаг регистрации'):
         common_functions_page.moving_from_the_second_step_to_the_third_step(page)
    with allure.step(f"Ввод значения в поле «Адрес места работы»: '{value}'"):
        third_step_of_registration_page.workplace_address_input.fill(value)
        third_step_of_registration_page.workplace_address_input.blur()
    with allure.step(f"Проверка: отображается ошибка '{expected_error}'"):
        if expected_error is None:
            expect(third_step_of_registration_page.error_message_necessary_fill_address_place_of_work).not_to_be_visible()
        else:
            expect(third_step_of_registration_page.error_message_necessary_fill_address_place_of_work).to_be_visible()
            actual_error = third_step_of_registration_page.error_message_necessary_fill_address_place_of_work.text_content()
            assert expected_error in actual_error, f'Ожидалось: "{expected_error}", отображается: "{actual_error}"'

@allure.epic("Веб-приложение OCM")
@allure.feature("Регистрация пользователя")
@allure.story("Проверка валидации третьей страницы регистрации")
@allure.title("Проверка поля 'Рабочий телефон'")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize(
    "value, expected_error, description",
    [
        ("9991234567", '+7 (999) 123-45-67', "валидно"),
        ("999123456", "Используйте формат: +7 (XXX) XXX-XX-XX", "невалидно"),
        ("9", "Используйте формат: +7 (XXX) XXX-XX-XX", "невалидно"),
        ("8", "Используйте формат: +7 (XXX) XXX-XX-XX", "невалидно"),
        ("Абвгд", "Используйте формат: +7 (XXX) XXX-XX-XX", "ввод заблокирован"),
        ("Latin", "Используйте формат: +7 (XXX) XXX-XX-XX", "ввод заблокирован"),
        ("$@%&#@", "Используйте формат: +7 (XXX) XXX-XX-XX", "ввод заблокирован"),
        ("", "Используйте формат: +7 (XXX) XXX-XX-XX", "невалидно"),
    ]
)
def test_worker_phone_input(page: Page, value: str, expected_error: str, description: str):
    third_step_of_registration_page = ThirdStepOfRegistrationPage(page)
    common_functions_page = CommonFunctionsPage(page)
    with allure.step('Вызываем функцию по заполению 1 шага регистрации и перехда на 2 шаг регистрации'):
         common_functions_page.moving_to_the_second_step(page)
    with allure.step('Вызываем функцию по заполению 2 шага регистрации и перехда на 3 шаг регистрации'):
         common_functions_page.moving_from_the_second_step_to_the_third_step(page)
    with allure.step(f"Ввод значения в поле «Адрес места работы»: '{value}'"):
        third_step_of_registration_page.work_phone_input.fill(value)
        third_step_of_registration_page.work_phone_input.blur()
    with allure.step(f"Проверка: отображается ошибка '{expected_error}'"):
        actual_formatted = third_step_of_registration_page.work_phone_input.input_value()
        if expected_error is '+7 (999) 123-45-67':
            assert actual_formatted == expected_error
            expect(third_step_of_registration_page.error_message_work_phone_format).not_to_be_visible()
        else:
            if 'ввод заблокирован' in description:
                expect(third_step_of_registration_page.error_message_work_phone_format).to_be_visible()
                expect(third_step_of_registration_page.work_phone_input).to_have_value('+7 (')
            else:
                expect(third_step_of_registration_page.error_message_work_phone_format).to_be_visible()
                actual_error = third_step_of_registration_page.error_message_work_phone_format.text_content()
                assert expected_error in actual_error, f'Ожидалось: "{expected_error}", отображается: "{actual_error}"'

'''
@allure.epic("Веб-приложение OCM")
@allure.feature("Регистрация пользователя")
@allure.story("Проверка валидации третьей страницы регистрации")
@allure.title("Проверка поля 'Среднемесячный доход (руб.)'")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize(
    "value, expected_error, description",
    [
        ("95000", None, "валидно"),
        ("Абвгд", "Необходимо заполнить «Среднемесячный доход (руб.)».", "ввод заблокирован"),
        ("Latin", "Необходимо заполнить «Среднемесячный доход (руб.)».", "ввод заблокирован"),
        ("$@%&#@", "Необходимо заполнить «Среднемесячный доход (руб.)».", "ввод заблокирован"),
        ("", "Необходимо заполнить «Среднемесячный доход (руб.)».", "невалидно"),
        ("-1", "Значение «Среднемесячный доход (руб.)» должно быть не меньше 0.", "меньше 0"),
        ("10000000", "Значение «Среднемесячный доход (руб.)» не должно превышать 1000000.", "больше 1000000"),
    ]
)
def test_family_income_input(page: Page, value: str, expected_error: str, description: str):
    third_step_of_registration_page = ThirdStepOfRegistrationPage(page)
    common_functions_page = CommonFunctionsPage(page)
    with allure.step('Вызываем функцию по заполению 1 шага регистрации и перехда на 2 шаг регистрации'):
         common_functions_page.moving_to_the_second_step(page)
    with allure.step('Вызываем функцию по заполению 2 шага регистрации и перехда на 3 шаг регистрации'):
         common_functions_page.moving_from_the_second_step_to_the_third_step(page)
    with allure.step(f"Ввод значения в поле «Адрес места работы»: '{value}'"):
        third_step_of_registration_page.family_income_input.fill(value) #\\ ошибка playwright._impl._errors.Error: Locator.fill: Error: Cannot type text into input[type=number]
        third_step_of_registration_page.family_income_input.blur()
    with allure.step(f"Проверка: отображается ошибка '{expected_error}'"):
        if expected_error is None:
            expect(third_step_of_registration_page.error_message_fill_averagemonthly_income).not_to_be_visible()
            expect(third_step_of_registration_page.error_message_averagemonthly_must_be_at_least_zero).not_to_be_visible()
            expect(third_step_of_registration_page.error_message_averagemonthly_should_not_exceed_millions).not_to_be_visible()
        else:
            if 'ввод заблокирован' in description:
                expect(third_step_of_registration_page.error_message_fill_averagemonthly_income).to_be_visible()
            else:
                if 'меньше 0' in description:
                    expect(third_step_of_registration_page.error_message_averagemonthly_must_be_at_least_zero).to_be_visible()
                else:
                    if 'больше 1000000' in description:
                        expect(third_step_of_registration_page.error_message_averagemonthly_should_not_exceed_millions).to_be_visible()
                    else:
                        expect(third_step_of_registration_page.error_message_fill_averagemonthly_income).to_be_visible()
                        actual_error = third_step_of_registration_page.error_message_fill_averagemonthly_income.text_content()
                        assert expected_error in actual_error, f'Ожидалось: "{expected_error}", отображается: "{actual_error}"'
'''
@allure.epic("Веб-приложение OCM")
@allure.feature("Регистрация пользователя")
@allure.story("Проверка валидации третьей страницы регистрации")
@allure.title("Проверка поля 'Среднемесячный доход (руб.)'")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize(
    "value, expected_value, error_locator",
    [
        ("95000", "95000", None),
        ("Абвгд", "", "fill"),
        ("Latin", "", "fill"),
        ("$@%&#@", "", "fill"),
        ("", "", "fill"),
        ("-1", "-1", "min"),
        ("1000001", "1000001", "max"),
    ]
)
def test_family_income_input(page: Page, value, expected_value, error_locator):
    third_step_of_registration_page = ThirdStepOfRegistrationPage(page)
    common_functions_page = CommonFunctionsPage(page)
    with allure.step('Вызываем функцию по заполению 1 шага регистрации и перехда на 2 шаг регистрации'):
        common_functions_page.moving_to_the_second_step(page)
    with allure.step('Вызываем функцию по заполению 2 шага регистрации и перехда на 3 шаг регистрации'):
        common_functions_page.moving_from_the_second_step_to_the_third_step(page)
    with allure.step(f"Ввод значения: {value}"):
        third_step_of_registration_page.family_income_input.click()
        third_step_of_registration_page.family_income_input.press("Control+A")
        third_step_of_registration_page.family_income_input.press("Delete")
        third_step_of_registration_page.family_income_input.press_sequentially(value)
        third_step_of_registration_page.family_income_input.blur()
    expect(third_step_of_registration_page.family_income_input).to_have_value(expected_value)
    errors = {
        "fill": third_step_of_registration_page.error_message_fill_averagemonthly_income,
        "min": third_step_of_registration_page.error_message_averagemonthly_must_be_at_least_zero,
        "max": third_step_of_registration_page.error_message_averagemonthly_should_not_exceed_millions
    }
    if error_locator:
        expect(errors[error_locator]).to_be_visible()
    else:
        for err in errors.values():
            expect(err).not_to_be_visible()

@allure.epic("Веб-приложение OCM")
@allure.feature("Регистрация пользователя")
@allure.story("Проверка валидации третьей страницы регистрации")
@allure.title("Проверка поля 'Текущий платеж по ипотеке, кредитам (0 - если нет)'")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize(
    "value, expected_value, error_locator",
    [
        ("55000", "55000", None),
        ("Абвгд", "", "fill"),
        ("Latin", "", "fill"),
        ("$@%&#@", "", "fill"),
        ("", "", "fill"),
        ("-1", "-1", "min"),
        ("1000001", "1000001", "max"),
    ]
)
def test_family_outgo_input(page: Page, value, expected_value, error_locator):
    third_step_of_registration_page = ThirdStepOfRegistrationPage(page)
    common_functions_page = CommonFunctionsPage(page)
    with allure.step('Вызываем функцию по заполению 1 шага регистрации и перехда на 2 шаг регистрации'):
        common_functions_page.moving_to_the_second_step(page)
    with allure.step('Вызываем функцию по заполению 2 шага регистрации и перехда на 3 шаг регистрации'):
        common_functions_page.moving_from_the_second_step_to_the_third_step(page)
    with allure.step(f"Ввод значения: {value}"):
        third_step_of_registration_page.family_outgo_input.click()
        third_step_of_registration_page.family_outgo_input.press("Control+A")
        third_step_of_registration_page.family_outgo_input.press("Delete")
        third_step_of_registration_page.family_outgo_input.press_sequentially(value)
        third_step_of_registration_page.family_outgo_input.blur()
    expect(third_step_of_registration_page.family_outgo_input).to_have_value(expected_value)
    errors = {
        "fill": third_step_of_registration_page.error_message_fill_mortgage_loan_payments_income,
        "min": third_step_of_registration_page.error_message_mortgage_loan_payments_must_be_at_least_zero,
        "max": third_step_of_registration_page.error_message_mortgage_loan_payments_should_not_exceed_millions
    }
    if error_locator:
        expect(errors[error_locator]).to_be_visible()
    else:
        for err in errors.values():
            expect(err).not_to_be_visible()

@allure.epic("Веб-приложение OCM")
@allure.feature("Регистрация пользователя")
@allure.story("Проверка валидации третьей страницы регистрации")
@allure.title("Проверка поля 'Дополнительный телефон'")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize(
    "value, expected_value, error_locator",
    [
        ("9991234567", "+7 (999) 123-45-67", None),
        ("999123456","+7 (999) 123-45-6","fill"),
        ("9","+7 (9","fill"),
        ("8","+7 (8","fill"),
        ("Абвгд", "+7 (", "fill"),
        ("Latin", "+7 (", "fill"),
        ("$@%&#@", "+7 (", "fill"),
        ("", "+7 (", "fill"),
    ]
)
def test_cohabitor_phone_input(page: Page, value, expected_value, error_locator):
    third_step_of_registration_page = ThirdStepOfRegistrationPage(page)
    common_functions_page = CommonFunctionsPage(page)
    with allure.step('Вызываем функцию по заполению 1 шага регистрации и перехда на 2 шаг регистрации'):
        common_functions_page.moving_to_the_second_step(page)
    with allure.step('Вызываем функцию по заполению 2 шага регистрации и перехда на 3 шаг регистрации'):
        common_functions_page.moving_from_the_second_step_to_the_third_step(page)
    with allure.step(f"Ввод значения: {value}"):
        third_step_of_registration_page.cohabitor_phone_input.fill(value)
        third_step_of_registration_page.cohabitor_phone_input.blur()
    expect(third_step_of_registration_page.cohabitor_phone_input).to_have_value(expected_value)
    errors = {
        "fill": third_step_of_registration_page.error_message_cohabitor_phone_format,
    }
    if error_locator:
        expect(errors[error_locator]).to_be_visible()
    else:
        for err in errors.values():
            expect(err).not_to_be_visible()

@allure.epic("Веб-приложение OCM")
@allure.feature("Регистрация пользователя")
@allure.story("Проверка валидации третьей страницы регистрации")
@allure.title("Проверка Успешное заполнение Шага 3 и переход на страницу активации")
@allure.severity(allure.severity_level.NORMAL)
def test_moving_from_the_third_step_to_the_activate_step(page: Page):
    third_step_of_registration_page = ThirdStepOfRegistrationPage(page)
    common_functions_page = CommonFunctionsPage(page)
    with allure.step('Вызываем функцию по заполению 1 шага регистрации и перехда на 2 шаг регистрации'):
        common_functions_page.moving_to_the_second_step(page)
    with allure.step('Вызываем функцию по заполению 2 шага регистрации и перехда на 3 шаг регистрации'):
        common_functions_page.moving_from_the_second_step_to_the_third_step(page)
    with allure.step('Вызываем функцию по заполению 3 шага регистрации и перехда на страницу активации'):
        common_functions_page.moving_from_the_third_step_to_the_activate_step(page)