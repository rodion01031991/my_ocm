import pytest
import allure
from playwright.sync_api import Page, expect
from pages.first_step_of_registration_page import FirstStepOfRegistrationPage


@allure.epic("Веб-приложение OCM")
@allure.feature("Регистрация пользователя")
@allure.story("Проверка валидации первой страницы регистрации")
@allure.title("Проверка обязательных полей на Шаге 1 при отправке пустой формы")
@allure.severity(allure.severity_level.CRITICAL)
def test_empty_fields_simple(page: Page):
    """Проверка обязательных полей на Шаге 1 при отправке пустой формы"""
    # 1. Подготовка
    first_step_of_registration_page = FirstStepOfRegistrationPage(page)
    with allure.step('Открыть страницу первого шага регистрации'):
        first_step_of_registration_page.open_first_step_of_registration()
    initial_url = page.url
    # 2. Проверка что поля пустые
    with allure.step('Проверка что поля пустые'):
        first_step_of_registration_page.verify_all_fields_are_empty()
    # 3. Действие
    with allure.step('Нажать на кнопку далее'):
        first_step_of_registration_page.click_next_step_button()
    # 4. Проверка 1: Не было перехода
    with allure.step('Проверка url страницы'):
        expect(page).to_have_url(initial_url)
    # 5. Проверка 2: Все ошибки отображаются
    with allure.step('Проверка что все ошибки отображаются'):
        first_step_of_registration_page.verify_all_error_messages_visible()


#Проверка чекбокса "Нет отчества по паспорту" на Шаге 1
@allure.epic("Веб-приложение OCM")
@allure.feature("Регистрация пользователя")
@allure.story("Проверка валидации первой страницы регистрации")
@allure.title("Проверка чекбокса 'Нет отчества по паспорту' на Шаге 1")
@allure.severity(allure.severity_level.NORMAL)
def test_no_middle_name_checkbox (page: Page):
    first_step_of_registration_page = FirstStepOfRegistrationPage(page)
    with allure.step('Открыть страницу первого шага регистрации'):
        first_step_of_registration_page.open_first_step_of_registration()
    with allure.step('Кликнуть на чекбокс "Нет отчества по паспорту"'):
        first_step_of_registration_page.click_no_middle_name_checkbox()
    with allure.step('Проверка что поле "Отчество" изчезло'):
        expect(first_step_of_registration_page.middle_name_input).not_to_be_visible()
    with allure.step('Кликнуть на чекбокс "Нет отчества по паспорту"'):
        first_step_of_registration_page.click_no_middle_name_checkbox()
    with allure.step('Проверка что поле "Отчество" появилось'):
        expect(first_step_of_registration_page.middle_name_input).to_be_visible()


#Проверка поля 'Фамилия' на Шаге 1
@allure.epic("Веб-приложение OCM")
@allure.feature("Регистрация пользователя")
@allure.story("Проверка валидации первой страницы регистрации")
@allure.title("Проверка поля 'Фамилия' на Шаге 1")
@allure.severity(allure.severity_level.NORMAL)
def test_surname_input(page: Page):
    first_step_of_registration_page = FirstStepOfRegistrationPage(page)
    with allure.step('Открыть страницу первого шага регистрации'):
        first_step_of_registration_page.open_first_step_of_registration()
    # Получаем тестовые кейсы
    with allure.step('Получаем тестовые кейсы'):
        test_cases = first_step_of_registration_page.get_test_cases_surname()
    for surname, expected_error, description in test_cases:
        with allure.step(f'Проверка: {description} (ввод: "{surname}")'):
            # Очистить поле
            first_step_of_registration_page.surname_input.clear()
            # Ввести значение
            if surname:
                first_step_of_registration_page.surname_input.fill(surname)
            # Убрать фокус
            first_step_of_registration_page.trigger_validation()
            # Проверить наличие/отсутствие ошибки
            if expected_error is None:
                # Ошибки быть не должно
                expect(first_step_of_registration_page.error_message_wrong_language).not_to_be_visible()
                expect(first_step_of_registration_page.error_message_surname).not_to_be_visible()
            else:
                # Определяем, какой тип ошибки ожидается
                if 'Необходимо заполнить «Фамилия».' in expected_error:
                    # Это ошибка пустого поля
                    expect(first_step_of_registration_page.error_message_surname).to_be_visible()
                    actual_error = first_step_of_registration_page.error_message_surname.text_content()
                else:
                    # Это ошибка о языке/символах
                    expect(first_step_of_registration_page.error_message_wrong_language).to_be_visible()
                    actual_error = first_step_of_registration_page.error_message_wrong_language.text_content()
                # Проверить текст ошибки
                assert expected_error in actual_error, \
 \
                    f'Текст ошибки не совпадает. Ожидалось: "{expected_error}", получено: "{actual_error}"'



#Проверка поля 'Имя' на Шаге 1
@allure.epic("Веб-приложение OCM")
@allure.feature("Регистрация пользователя")
@allure.story("Проверка валидации первой страницы регистрации")
@allure.title("Проверка поля 'Имя' на Шаге 1")
@allure.severity(allure.severity_level.NORMAL)
def test_name_input(page: Page):

    first_step_of_registration_page = FirstStepOfRegistrationPage(page)

    with allure.step('Открыть страницу первого шага регистрации'):
        first_step_of_registration_page.open_first_step_of_registration()

    # Получаем тестовые кейсы
    with allure.step('Получаем тестовые кейсы'):
        test_cases = first_step_of_registration_page.get_test_cases_first_name()

    for name, expected_error, description in test_cases:
        with allure.step(f'Проверка: {description} (ввод: "{name}")'):
            # Очистить поле
            first_step_of_registration_page.first_name_input.clear()

            # Ввести значение
            if name:
                first_step_of_registration_page.first_name_input.fill(name)

            # Убрать фокус для триггера валидации
            first_step_of_registration_page.trigger_validation()

            # Проверить наличие/отсутствие ошибки
            if expected_error is None:
                # Ошибки быть не должно
                expect(first_step_of_registration_page.error_message_wrong_language).not_to_be_visible()
                expect(first_step_of_registration_page.error_message_name).not_to_be_visible()


            else:

                # Определяем, какой тип ошибки ожидается

                if 'Необходимо заполнить «Имя».' in expected_error:

                    # Это ошибка пустого поля

                    expect(first_step_of_registration_page.error_message_name).to_be_visible()

                    actual_error = first_step_of_registration_page.error_message_name.text_content()

                else:

                    # Это ошибка о языке/символах

                    expect(first_step_of_registration_page.error_message_wrong_language).to_be_visible()

                    actual_error = first_step_of_registration_page.error_message_wrong_language.text_content()

                # Проверить текст ошибки

                assert expected_error in actual_error, \
 \
                    f'Текст ошибки не совпадает. Ожидалось: "{expected_error}", получено: "{actual_error}"'



#Проверка поля 'Отчество' на Шаге 1
@allure.epic("Веб-приложение OCM")
@allure.feature("Регистрация пользователя")
@allure.story("Проверка валидации первой страницы регистрации")
@allure.title("Проверка поля 'Отчество' на Шаге 1")
@allure.severity(allure.severity_level.NORMAL)
def test_middle_name_input(page: Page):

    first_step_of_registration_page = FirstStepOfRegistrationPage(page)

    with allure.step('Открыть страницу первого шага регистрации'):
        first_step_of_registration_page.open_first_step_of_registration()

        # Получаем тестовые кейсы
        with allure.step('Получаем тестовые кейсы'):
            test_cases = first_step_of_registration_page.get_test_cases_middle_name()

    for middle_name, expected_error, description in test_cases:
        with allure.step(f'Проверка: {description} (ввод: "{middle_name}")'):
            # Очистить поле
            first_step_of_registration_page.middle_name_input.clear()

            # Ввести значение
            if middle_name:
                first_step_of_registration_page.middle_name_input.fill(middle_name)

            # Убрать фокус для триггера валидации
            first_step_of_registration_page.trigger_validation()

            # Проверить наличие/отсутствие ошибки
            if expected_error is None:
                # Ошибки быть не должно
                expect(first_step_of_registration_page.error_message_wrong_language).not_to_be_visible()
                expect(first_step_of_registration_page.error_message_middle_name).not_to_be_visible()


            else:

                # Определяем, какой тип ошибки ожидается

                if 'В случае отсутствия установите «Нет отчества как в паспорте»' in expected_error:

                    # Это ошибка пустого поля

                    expect(first_step_of_registration_page.error_message_middle_name).to_be_visible()

                    actual_error = first_step_of_registration_page.error_message_middle_name.text_content()

                else:

                    # Это ошибка о языке/символах

                    expect(first_step_of_registration_page.error_message_wrong_language).to_be_visible()

                    actual_error = first_step_of_registration_page.error_message_wrong_language.text_content()

                # Проверить текст ошибки

                assert expected_error in actual_error, \
 \
                    f'Текст ошибки не совпадает. Ожидалось: "{expected_error}", получено: "{actual_error}"'



#Проверка поля 'Дата рождения' на Шаге 1
@allure.epic("Веб-приложение OCM")
@allure.feature("Регистрация пользователя")
@allure.story("Проверка валидации первой страницы регистрации")
@allure.title("Проверка поля 'Дата рождения' на Шаге 1")
@allure.severity(allure.severity_level.NORMAL)
def test_date_of_birth_input(page: Page):

    first_step_of_registration_page = FirstStepOfRegistrationPage(page)

    with allure.step('Открыть страницу первого шага регистрации'):
        first_step_of_registration_page.open_first_step_of_registration()

        # Получаем тестовые кейсы
        with allure.step('Получаем тестовые кейсы'):
            test_cases = first_step_of_registration_page.get_test_cases_date_of_birth()

    for date_of_birth, expected_error, description in test_cases:
        with allure.step(f'Проверка: {description} (ввод: "{date_of_birth}")'):
            # Очистить поле
            first_step_of_registration_page.date_of_birth_input.clear()

            # Ввести значение
            if date_of_birth:
                first_step_of_registration_page.date_of_birth_input.fill(date_of_birth)

            # Убрать фокус для триггера валидации
            first_step_of_registration_page.trigger_validation()

            # Проверить наличие/отсутствие ошибки
            if expected_error is None:
                # Ошибки быть не должно
                expect(first_step_of_registration_page.error_message_date_of_birth).not_to_be_visible()
                expect(first_step_of_registration_page.error_message_incorrect_format_date_of_birth).not_to_be_visible()


            else:

                # Определяем, какой тип ошибки ожидается

                if 'Неправильный формат даты' in expected_error:

                    # Это ошибка Неправильный формат даты

                    expect(first_step_of_registration_page.error_message_incorrect_format_date_of_birth).to_be_visible()

                    actual_error = first_step_of_registration_page.error_message_incorrect_format_date_of_birth.text_content()

                else:

                    # Это ошибка о необходимости заполнить Дату рождения

                    expect(first_step_of_registration_page.error_message_date_of_birth).to_be_visible()

                    expect(first_step_of_registration_page.date_of_birth_input).to_be_empty()

                    actual_error = first_step_of_registration_page.error_message_date_of_birth.text_content()

                # Проверить текст ошибки

                assert expected_error in actual_error, \
 \
                    f'Текст ошибки не совпадает. Ожидалось: "{expected_error}", получено: "{actual_error}"'

#Проверка радиобатон Женщина на первом шаги регистрации
@allure.epic("Веб-приложение OCM")
@allure.feature("Регистрация пользователя")
@allure.story("Выбор пола на первом шаге регистрации")
@allure.title("Выбор женского пола в форме регистрации")
@allure.severity(allure.severity_level.NORMAL)
def test_select_woman_gender(page: Page):
    first_step_of_registration_page = FirstStepOfRegistrationPage(page)
    # Шаг 1: Открыть страницу регистрации
    with allure.step('Открыть страницу первого шага регистрации'):
        first_step_of_registration_page.open_first_step_of_registration()
    # Шаг 2: Кликнуть на радиобатон "Женщина"
    with allure.step("Кликнуть на радиобатон 'Женщина'"):
        first_step_of_registration_page.select_woman_gender_radiobaton()
    # Шаг 3: Проверить активацию радиобатона
    with allure.step("Проверить что радиобатон 'Женщина' активирован"):
        first_step_of_registration_page.is_woman_gender_selected()



#Проверка радиобатон Мужчина на первом шаги регистрации
@allure.epic("Веб-приложение OCM")
@allure.feature("Регистрация пользователя")
@allure.story("Выбор пола на первом шаге регистрации")
@allure.title("Выбор мужского пола в форме регистрации")
@allure.severity(allure.severity_level.NORMAL)
def test_select_man_gender(page: Page):
    first_step_of_registration_page = FirstStepOfRegistrationPage(page)
    # Шаг 1: Открыть страницу регистрации
    with allure.step('Открыть страницу первого шага регистрации'):
        first_step_of_registration_page.open_first_step_of_registration()
    # Шаг 2: Кликнуть на радиобатон "Женщина"
    with allure.step("Кликнуть на радиобатон 'Женщина'"):
        first_step_of_registration_page.select_woman_gender_radiobaton()
    # Шаг 3: Кликнуть на радиобатон "Мужчина"
    with allure.step("Кликнуть на радиобатон 'Мужчина'"):
        first_step_of_registration_page.select_man_gender_radiobaton()
    # Шаг 4: Проверить активацию радиобатона
    with allure.step("Проверить что радиобатон 'Мужчина' активирован"):
        first_step_of_registration_page.is_man_gender_selected()


#Проверка поля 'Мобильный телефон' на Шаге 1
@allure.epic("Веб-приложение OCM")
@allure.feature("Регистрация пользователя")
@allure.story("Проверка валидации первой страницы регистрации")
@allure.title("Проверка поля 'Мобильный телефон' на Шаге 1")
@allure.severity(allure.severity_level.NORMAL)
def test_mobile_phone_input(page: Page):

    first_step_of_registration_page = FirstStepOfRegistrationPage(page)

    with allure.step('Открыть страницу первого шага регистрации'):
        first_step_of_registration_page.open_first_step_of_registration()

        # Получаем тестовые кейсы
        with allure.step('Получаем тестовые кейсы'):
            test_cases = first_step_of_registration_page.get_test_cases_mobile_phone()

    for mobile_phone, expected_error, description in test_cases:
        with allure.step(f'Проверка: {description} (ввод: "{mobile_phone}")'):
            # Очистить поле
            first_step_of_registration_page.mobile_phone_input.clear()

            # Ввести значение
            if mobile_phone:
                first_step_of_registration_page.mobile_phone_input.fill(mobile_phone)

            # Убрать фокус для триггера валидации
            first_step_of_registration_page.trigger_validation()

            # Проверить форматированиеи и отсутсвие ошибки
            actual_formatted = first_step_of_registration_page.mobile_phone_input.input_value()
            if expected_error == '+7 (999) 123-45-67':
                # Ошибки быть не должно
                assert actual_formatted == expected_error
                expect(first_step_of_registration_page.error_message_mobile_phone_format).not_to_be_visible()
            else:
                expect(first_step_of_registration_page.error_message_mobile_phone_format).to_be_visible()
                actual_error = first_step_of_registration_page.error_message_mobile_phone_format.text_content()

                # Проверить текст ошибки
                assert expected_error in actual_error, \
 \
                    f'Текст ошибки не совпадает. Ожидалось: "{expected_error}", получено: "{actual_error}"'