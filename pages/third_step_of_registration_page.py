import typing
from typing import Literal

from playwright._impl._api_structures import Position
from playwright.sync_api import Page, expect
from pages.common_functions_page import CommonFunctionsPage
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
        self.checkbox_is_workless = page.locator('label[for="usermodel-is_workless"]')
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
        self.next_button = page.get_by_text('следующим', exact=True)
        # Чекбокс "Предоставление персональных данных"
        self.checkbox_is_provision_of_personal_data = page.locator('div#check_4')
        # Чекбокс "Не согласен на уступку Займодавцем своих прав (требования) по договору микрозайма третьим лицам"
        self.checkbox_other_parties_no = page.locator('#check_other_parties_no')
        # Чекбокс "Cогласен на уступку Займодавцем своих прав (требования) по договору микрозайма третьим лицам"
        self.checkbox_other_parties_yes = page.locator('#check_other_parties_yes')
        # Чекбокс "Я согласен на получение информации рекламного характера"
        self.checkbox_advertising_information = page.locator('#check_3')
        # Чекбокс "До направления Заявления до меня доведена информация о том"
        self.checkbox_do_before_submitting_application = page.locator('#check_5')
        # Чекбокс "Согласен с обращением АО «МКК УФ» в Бюро кредитных историй"
        self.checkbox_credit_history_mfo_yes = page.locator('#check_creditHistoryMFO_yes')
        # Чекбокс "Не согласен с обращением АО «МКК УФ» в Бюро кредитных историй"
        self.checkbox_credit_history_mfo_no = page.locator('#check_creditHistoryMFO_no')
        # Чекбокс "Настоящим, я даю согласие на подключение сервиса «Автоплатеж»"
        self.checkbox_autopayments = page.locator('#check_recurrent')

    # Проставить чекбокс "Официально не трудоустроен"
    def check_checkbox_is_workless(self):
        self.checkbox_is_workless.check()

    # Снять чекбокс "Официально не трудоустроен"
    def uncheck_checkbox_is_workless(self):
        self.checkbox_is_workless.uncheck()

    # Проверка что поля "Место работы" "Адрес места работы" "Рабочий телефон" не отображаются'
    def verify_input_not_visible(self):
        expect(self.place_of_work_input).not_to_be_visible()
        expect(self.workplace_address_input).not_to_be_visible()
        expect(self.work_phone_input).not_to_be_visible()

    # Проверка что поля "Место работы" "Адрес места работы" "Рабочий телефон" отображаются'
    def verify_input_visible(self):
        expect(self.place_of_work_input).to_be_visible()
        expect(self.workplace_address_input).to_be_visible()
        expect(self.work_phone_input).to_be_visible()

    # Нажать на кнопку "следующим"
    def click_next_button(self):
        self.next_button.click()

    # Проверка чекбоксов на 3 шаге регистрации
    def checking_the_checkboxes_third_registration_step(self):
        expect(self.checkbox_is_provision_of_personal_data).to_be_visible()
        expect(self.checkbox_other_parties_no).to_be_visible()
        expect(self.checkbox_other_parties_yes).to_be_visible()
        expect(self.checkbox_advertising_information).to_be_visible()
        expect(self.checkbox_do_before_submitting_application).to_be_visible()
        expect(self.checkbox_credit_history_mfo_yes).to_be_visible()
        expect(self.checkbox_credit_history_mfo_no).to_be_visible()
        expect(self.checkbox_autopayments).to_be_visible()












