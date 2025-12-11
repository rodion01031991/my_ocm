from playwright.sync_api import Page, expect
from faker import Faker

class FirstStepOfRegistrationPage(Page):
    BASE_URL = 'https://rc.dev.oneclickmoney.ru/registration/first/?Resident'
    fake_ru = Faker('ru_RU')
    fake_en = Faker('en_US')
    def __init__(self, page: Page):
        self.page = page
        #Поля ввода
        self.surname_input = page.locator('#usermodel-last_name')
        self.first_name_input = page.locator('#usermodel-first_name')
        self.middle_name_input = page.locator('#usermodel-middle_name')
        self.date_of_birth_input = page.locator('#usermodel-birth_date')
        self.mobile_phone_input = page.locator('#usermodel-mobile_phone')
        self.email_input = page.locator('#usermodel-email')
        self.password_input = page.locator('#usermodel-password')
        self.repeat_the_password_input = page.locator('#usermodel-confirm_password')
        #Чекбокс 'Нет отчества по паспорту'
        self.no_middle_name_checkbox = page.locator('label[for="usermodel-isnomiddlename"]')
        #Радиобаттоны пола
        self.man_gender_radiobaton = page.locator('label[for="usermodel-gender-key_1"]')
        self.woman_gender_radiobaton = page.locator('label[for="usermodel-gender-key_2"]')
        #Сообщения об ошибках
        self.error_message_wrong_language = page.locator('.error-page-field:has-text("Используйте только русские буквы и тире (допускается два слова через пробел")')
        self.error_message_surname = page.locator('.error-page-field:has-text("Необходимо заполнить «Фамилия».")')
        self.error_message_name = page.locator('.error-page-field:has-text("Необходимо заполнить «Имя».")')
        self.error_message_middle_name = page.locator('.error-page-field:has-text("В случае отсутствия установите «Нет отчества как в паспорте»")')
        self.error_message_date_of_birth = page.locator('.error-page-field:has-text("Необходимо заполнить «Дата рождения».")')
        self.error_message_incorrect_format_date_of_birth = page.locator('.error-page-field:has-text("Неправильный формат даты")')
        self.error_message_mobile_phone = page.locator('.error-page-field:has-text("Необходимо заполнить «Мобильный телефон».")')
        self.error_message_mobile_phone_format = page.locator('.error-page-field:has-text("Используйте формат: +7 (9XX) XXX-XX-XX")')
        self.error_message_email = page.locator('.error-page-field:has-text("Необходимо заполнить «E-mail».")')
        self.error_message_email_not_correct = page.locator('.error-page-field:has-text("Значение «E-mail» не является правильным email адресом.")')
        self.error_message_password = page.locator('.error-page-field:has-text("Необходимо заполнить «Пароль».")')
        self.error_message_repeat_the_password = page.locator('.error-page-field:has-text("Необходимо заполнить «Повторите пароль».")')
        self.error_message_small_password = page.locator('.error-page-field:has-text("Значение «Пароль» должно содержать минимум 6 символов.")')
        self.error_message_small_repeat_the_password = page.locator('.error-page-field:has-text("Значение «Повторите пароль» должно содержать минимум 6 символов.")')
        self.error_message_dont_match_password = page.locator('.error-page-field:has-text("Пароли должны совпадать")')
        #Кнопка дальше
        self.next_step_button = page.locator('#next-step-button')


    #Открыть первый шаг страницы регистрации
    def open_first_step_of_registration(self):
        self.page.goto(self.BASE_URL)


    #Нажать кнопку 'Далее'
    def click_next_step_button(self):
        self.next_step_button.click()


    #Проверить, что все поля формы пустые
    def verify_all_fields_are_empty(self):
        expect(self.surname_input).to_be_empty()
        expect(self.first_name_input).to_be_empty()
        expect(self.middle_name_input).to_be_empty()
        expect(self.date_of_birth_input).to_be_empty()
        expect(self.mobile_phone_input).to_be_empty()
        expect(self.email_input).to_be_empty()
        expect(self.password_input).to_be_empty()
        expect(self.repeat_the_password_input).to_be_empty()


    #Проверить, что все сообщения об ошибках отображаются
    def verify_all_error_messages_visible(self):

        expect(self.error_message_surname).to_be_visible()
        expect(self.error_message_name).to_be_visible()
        expect(self.error_message_middle_name).to_be_visible()
        expect(self.error_message_date_of_birth).to_be_visible()
        expect(self.error_message_mobile_phone).to_be_visible()
        expect(self.error_message_email).to_be_visible()
        expect(self.error_message_password).to_be_visible()
        expect(self.error_message_repeat_the_password).to_be_visible()


    # Кликнуть на чекбокс 'Нет отчества по паспорту'
    def click_no_middle_name_checkbox(self):
        self.no_middle_name_checkbox.click()


    #Кликнуть на радиобатон 'Женщина'
    def select_woman_gender_radiobaton(self):
        self.woman_gender_radiobaton.click()
        return self

    #Проверить выбран ли женский пол
    def is_woman_gender_selected(self) -> bool:
        return self.woman_gender_radiobaton.is_checked()


    # Кликнуть на радиобатон 'Мужчина'
    def select_man_gender_radiobaton(self):
        self.man_gender_radiobaton.click()
        return self

    # Проверить выбран ли мужской пол
    def is_man_gender_selected(self) -> bool:
        return self.man_gender_radiobaton.is_checked()

    #Очистка всех полей
    """def clear_field(self, field_name: str):
        fields = {
            'surname': self.surname_input,
            'name': self.name_input,
            'middle_name': self.middle_name_input,
            'birth_date': self.date_of_birth_input,
            'phone': self.mobile_phone_input,
            'email': self.email_input,
            'password': self.password_input,
            'repeat_password': self.repeat_the_password_input,
        }

        if field_name in fields:
            fields[field_name].clear()
        else:
            raise ValueError(f"Поле '{field_name}' не найдено")"""


    #Форматирование телефона
    '''def test_format_mobile_namber():
        # phone number in a string
        phonenumber_string = "9991234567"

        # parse string to a PhoneNumber object
        phone_number = phonenumbers.parse(f"+7{phonenumber_string}", "RU")

        # format PhoneNumber to INTERNATIONAL

        formatted = phonenumbers.format_number(phone_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        print('INTERNATIONAL Format :', formatted)
        '''

    # Убрать фокус для триггера валидации
    def trigger_validation(self):
        """Снять фокус с поля для триггера валидации"""

        # Проверяем активно ли поле "Имя"
        if self.first_name_input.evaluate('element => document.activeElement === element'):
            # Если поле Имя активно, кликаем на поле Фамилия
            self.surname_input.click()
        else:
            # Если поле Имя не активно, кликаем на него
            self.first_name_input.click()

        # Задержка для срабатывания валидации
        self.page.wait_for_timeout(300)


    #Тестовые данные для поля "Фамилия"
    def get_test_cases_surname(self):
        """Получить тестовые кейсы для валидации фамилии"""
        return [
            # (фамилия, ожидаемая_ошибка, описание)
            ('Иванов', None, 'Кириллица - валидно'),
            ('Ivanov', 'Используйте только русские буквы и тире (допускается два слова через пробел', 'Латиница - невалидно'),
            ('123', 'Используйте только русские буквы и тире (допускается два слова через пробел', 'Цифры - невалидно'),
            ('Ив@нов', 'Используйте только русские буквы и тире (допускается два слова через пробел', 'Спецсимвол - невалидно'),
            ('', 'Необходимо заполнить «Фамилия».', 'Пустое поле - невалидно'),
            ('Иванов-Петров', None, 'Двойная фамилия с дефисом - валидно'),
        ]

    #Тестовые данные для поля "Имя"
    def get_test_cases_first_name(self):
        """Получить тестовые кейсы для валидации имини"""
        return [
            # (Имя, ожидаемая_ошибка, описание)
            ('Иван', None, 'Кириллица - валидно'),
            ('Ivan', 'Используйте только русские буквы и тире (допускается два слова через пробел', 'Латиница - невалидно'),
            ('123', 'Используйте только русские буквы и тире (допускается два слова через пробел', 'Цифры - невалидно'),
            ('Ив@н', 'Используйте только русские буквы и тире (допускается два слова через пробел', 'Спецсимвол - невалидно'),
            ('', 'Необходимо заполнить «Имя».', 'Пустое поле - невалидно'),
            ('Иван-Ваня', None, 'Двойное имя с дефисом - валидно'),
        ]

    #Тестовые данные для поля "Отчество"
    def get_test_cases_middle_name(self):
        """Получить тестовые кейсы для валидации отчества"""
        return [
            # (отчество, ожидаемая_ошибка, описание)
            ('Иванович', None, 'Кириллица - валидно'),
            ('Ivanovich', 'Используйте только русские буквы и тире (допускается два слова через пробел', 'Латиница - невалидно'),
            ('123', 'Используйте только русские буквы и тире (допускается два слова через пробел', 'Цифры - невалидно'),
            ('Ив@нович', 'Используйте только русские буквы и тире (допускается два слова через пробел', 'Спецсимвол - невалидно'),
            ('', 'В случае отсутствия установите «Нет отчества как в паспорте»', 'Пустое поле - невалидно'),
            ('Иванович-Петрович', None, 'Двойное отчество с дефисом - валидно'),
        ]

    #Тестовые данные для поля "Дата рождения"
    def get_test_cases_date_of_birth(self):
        """Получить тестовые кейсы для даты рождения """
        return [
            # (дата рождения, ожидаемая_ошибка, описание)
            ('01.08.2000', None, 'Полная дата - валидно'),
            ('ДатаРожд', 'Необходимо заполнить «Дата рождения».', 'Кириллица - невалидно/ввод заблокирован'),
            ('DataRojd', 'Необходимо заполнить «Дата рождения».', 'Латиница - невалидно/ввод заблокирован'),
            ('#$%#@', 'Необходимо заполнить «Дата рождения».', 'Спецсимвол - невалидно/ввод заблокирован'),
            ('05.01.20', 'Неправильный формат даты', 'Не полная дата - невалидно'),
            ('', 'Необходимо заполнить «Дата рождения».', 'Пустое поле - невалидно'),
        ]

    #Тестовые данные для поля "Мобильный телефон"
    def get_test_cases_mobile_phone(self):
        """Получить тестовые кейсы для мобильный телефон """
        return [
            # (мобильный телефон, ожидаемая_ошибка, описание)
            ('9991234567', '+7 (999) 123-45-67', 'валидно, форматируется в +7(999)123-45-67'),
            ('999123456', 'Используйте формат: +7 (9XX) XXX-XX-XX', '9 цифр - невалидно'),
            ('9', 'Используйте формат: +7 (9XX) XXX-XX-XX', 'Одна цифра - невалидно'),
            ('8', 'Используйте формат: +7 (9XX) XXX-XX-XX', 'Начало номера с 0-8 - невалидно'),
            ('Абвгд', 'Используйте формат: +7 (9XX) XXX-XX-XX', 'Кириллица - невалидно/ввод заблокирован'),
            ('Latin', 'Используйте формат: +7 (9XX) XXX-XX-XX', 'Латиница - невалидно/ввод заблокирован'),
            ('$@%&#@', 'Используйте формат: +7 (9XX) XXX-XX-XX', 'Спецсимвол - невалидно/ввод заблокирован'),
            ('', 'Используйте формат: +7 (9XX) XXX-XX-XX', 'Пустое поле - невалидно'),
        ]