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
    #with allure.step('Проверяем наличие чекбоксов'):
        #third_step_of_registration_page.checking_the_checkboxes_third_registration_step()







