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
    from pages.first_step_of_registration_page import FirstStepOfRegistrationPage

    first_step_of_registration_page = FirstStepOfRegistrationPage(page)

    with allure.step('Открыть страницу первого шага регистрации'):
        first_step_of_registration_page.open_first_step_of_registration()

    # Тестовые данные и ожидаемые результаты
    test_cases = [
        # (фамилия, ожидаемая_ошибка, описание)
        ('Иванов', None, 'Кириллица - валидно'),
        ('Ivanov', 'Используйте только русские буквы и тире (допускается два слова через пробел',
         'Латиница - невалидно'),
        ('123', 'Используйте только русские буквы и тире (допускается два слова через пробел', 'Цифры - невалидно'),
        ('Ив@нов', 'Используйте только русские буквы и тире (допускается два слова через пробел',
         'Спецсимвол - невалидно'),
        ('', 'Необходимо заполнить «Фамилия».', 'Пустое поле - невалидно'),
        ('Иванов-Петров', None, 'Двойная фамилия с дефисом - валидно'),
    ]

    for surname, expected_error, description in test_cases:
        with allure.step(f'Проверка: {description} (ввод: "{surname}")'):
            # Очистить поле
            first_step_of_registration_page.surname_input.clear()

            # Ввести значение
            if surname:
                first_step_of_registration_page.surname_input.fill(surname)

            # Убрать фокус для триггера валидации
            first_step_of_registration_page.name_input.click()
            page.wait_for_timeout(300)

            # Проверить наличие/отсутствие ошибки
            if expected_error is None:
                # Ошибки быть не должно
                expect(first_step_of_registration_page.error_message_wrong_language).not_to_be_visible()


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
    from pages.first_step_of_registration_page import FirstStepOfRegistrationPage

    first_step_of_registration_page = FirstStepOfRegistrationPage(page)

    with allure.step('Открыть страницу первого шага регистрации'):
        first_step_of_registration_page.open_first_step_of_registration()

    # Тестовые данные и ожидаемые результаты
    test_cases = [
        # (фамилия, ожидаемая_ошибка, описание)
        ('Иван', None, 'Кириллица - валидно'),
        ('Ivan', 'Используйте только русские буквы и тире (допускается два слова через пробел',
         'Латиница - невалидно'),
        ('123', 'Используйте только русские буквы и тире (допускается два слова через пробел', 'Цифры - невалидно'),
        ('Ив@н', 'Используйте только русские буквы и тире (допускается два слова через пробел',
         'Спецсимвол - невалидно'),
        ('', 'Необходимо заполнить «Имя».', 'Пустое поле - невалидно'),
        ('Иван-Ваня', None, 'Двойное имя с дефисом - валидно'),
    ]

    for name, expected_error, description in test_cases:
        with allure.step(f'Проверка: {description} (ввод: "{name}")'):
            # Очистить поле
            first_step_of_registration_page.name_input.clear()

            # Ввести значение
            if name:
                first_step_of_registration_page.name_input.fill(name)

            # Убрать фокус для триггера валидации
            first_step_of_registration_page.surname_input.click()
            page.wait_for_timeout(300)

            # Проверить наличие/отсутствие ошибки
            if expected_error is None:
                # Ошибки быть не должно
                expect(first_step_of_registration_page.error_message_wrong_language).not_to_be_visible()


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
    from pages.first_step_of_registration_page import FirstStepOfRegistrationPage

    first_step_of_registration_page = FirstStepOfRegistrationPage(page)

    with allure.step('Открыть страницу первого шага регистрации'):
        first_step_of_registration_page.open_first_step_of_registration()

    # Тестовые данные и ожидаемые результаты
    test_cases = [
        # (фамилия, ожидаемая_ошибка, описание)
        ('Иванович', None, 'Кириллица - валидно'),
        ('Ivanovich', 'Используйте только русские буквы и тире (допускается два слова через пробел',
         'Латиница - невалидно'),
        ('123', 'Используйте только русские буквы и тире (допускается два слова через пробел', 'Цифры - невалидно'),
        ('Ив@нович', 'Используйте только русские буквы и тире (допускается два слова через пробел',
         'Спецсимвол - невалидно'),
        ('', 'В случае отсутствия установите «Нет отчества как в паспорте»', 'Пустое поле - невалидно'),
        ('Иванович-Петрович', None, 'Двойное отчество с дефисом - валидно'),
    ]

    for middle_name, expected_error, description in test_cases:
        with allure.step(f'Проверка: {description} (ввод: "{middle_name}")'):
            # Очистить поле
            first_step_of_registration_page.middle_name_input.clear()

            # Ввести значение
            if middle_name:
                first_step_of_registration_page.middle_name_input.fill(middle_name)

            # Убрать фокус для триггера валидации
            first_step_of_registration_page.surname_input.click()
            page.wait_for_timeout(300)

            # Проверить наличие/отсутствие ошибки
            if expected_error is None:
                # Ошибки быть не должно
                expect(first_step_of_registration_page.error_message_wrong_language).not_to_be_visible()


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