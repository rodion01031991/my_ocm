from playwright.sync_api import Page, expect
from faker import Faker
fake_ru = Faker('ru_RU')
fake_en = Faker('en_US')

class ThirdStepOfRegistrationPage(Page):
    URL_FIRST_STEP = 'https://rc.dev.oneclickmoney.ru/registration/first/?Resident'
    URL_SECOND_STEP = 'https://rc.dev.oneclickmoney.ru/registration/second/'
    URL_THIRD_STEP = 'https://rc.dev.oneclickmoney.ru/registration/third/'
    def __init__(self, page: Page):
        self.page = page
        # Чекбокс "Официально не трудоустроен"
        self.checkbox_is_workless = page.locator('#usermodel-is_workless')
        # Чекбокс "Пенсионер"
        self.checkbox_pensioner = page.locator('#usermodel-pensioner')
        # Поле ввода "Место работы"
        self.place_of_work_input = page.locator('#usermodel-work_place')
        # Поле ввода "Адрес места работы"
        self.workplace_address_input = page.locator('#usermodel-work_place_address')
        # Поле ввода "Рабочий телефон"
        self.work_phone_input = page.locator('#usermodel-work_phone')
        # Поле ввода "Среднемесячный доход (руб.)"
        self.family_income_input = page.locator('#usermodel-family_income')
        # Поле ввода "Текущий платеж по ипотеке, кредитам (0 - если нет)"
        self.family_outgo_input = page.locator('#usermodel-family_outgo')
        # Поле ввода "Дополнительный телефон"
        self.cohabitor_phone_input = page.locator('#usermodel-cohabitor_phone')
        # Чекбокс "Настоящим я подтверждаю, что ознакомлен и согласен со "
        self.checkbox_global = page.locator('#check_global')
        # Кнопка(аккордеон) "следующим"
        self.next_button = page.locator('#registration-three__checkbox-label registration-three__checkbox-label--button registration-three__checkbox-btn-modify')



















