from playwright.sync_api import Page, expect

class FirstStepOfRegistrationPage(Page):
    BASE_URL = 'https://rc.dev.oneclickmoney.ru/registration/first/?Resident'
    def __init__(self, page: Page):
        self.page = page
        #Поля ввода
        self.surname_input = page.locator('#usermodel-last_name')
        self.name_input = page.locator('#usermodel-first_name')
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
        expect(self.name_input).to_be_empty()
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


    """def surname_input_data(self, surname: str):
        self.surname_input.fill(surname)
        self.name_input.click()"""