from playwright.sync_api import Page, expect
import allure
from faker import Faker
fake_ru = Faker('ru_RU')
fake_en = Faker('en_US')

class CommonFunctionsPage(Page):
    URL_FIRST_STEP = 'https://rc.dev.oneclickmoney.ru/registration/first/?Resident'
    URL_SECOND_STEP = 'https://rc.dev.oneclickmoney.ru/registration/second/'
    URL_THIRD_STEP = 'https://rc.dev.oneclickmoney.ru/registration/third/'
    URL_ACTIVATE_STEP = 'https://rc.dev.oneclickmoney.ru/registration/activate/'
    def __init__(self, page: Page):
        self.page = page
        # Поля ввода 1 шага регистрации
        self.surname_input = page.locator('#usermodel-last_name')
        self.first_name_input = page.locator('#usermodel-first_name')
        self.middle_name_input = page.locator('#usermodel-middle_name')
        self.date_of_birth_input = page.locator('#usermodel-birth_date')
        self.mobile_phone_input = page.locator('#usermodel-mobile_phone')
        self.email_input = page.locator('#usermodel-email')
        self.password_input = page.locator('#usermodel-password')
        self.repeat_the_password_input = page.locator('#usermodel-confirm_password')
        self.next_step_button = page.locator('#next-step-button')
        # Поля ввода 2 шага регистрации
        self.pass_num_input = page.locator('#usermodel-passport_number')
        self.pass_code_input = page.locator('#usermodel-passport_issuer_code')
        self.pass_name_input = page.locator('#usermodel-passport_issuer_name')
        self.pass_date_input = page.locator('#usermodel-passport_date')
        self.pass_birthplace_input = page.locator('#usermodel-passport_birth_place')
        self.region_input = page.locator('#usermodel-region')
        self.city_input = page.locator('#usermodel-city')
        self.street_input = page.locator('#usermodel-street')
        self.house_num_input = page.locator('#usermodel-house_number')
        self.next_step_button_second = page.locator('.registration-two__submit')
        # Поля ввода 3 шага регистрации
        # Поле ввода "Место работы"
        self.place_of_work_input = page.locator('#usermodel-work_place')
        # Поле ввода "Адрес места работы"
        self.workplace_address_input = page.locator('#usermodel-work_place_address')
        # Поле ввода "Рабочий телефон"
        self.work_phone_input = page.locator('#usermodel-work_phone')
        # Поле ввода "Среднемесячный доход (руб.)"
        self.family_income_input = page.locator('#usermodel-family_income')
        # Поле ввода "Дополнительный телефон"
        self.cohabitor_phone_input = page.locator('#usermodel-cohabitor_phone')
        # Кнопка "Отправить заявку"
        self.button_send_request = page.get_by_role("button", name="Отправить заявку")


  #Генерация данных для первого шага регистрации
    def generate_test_cases_first_step_of_registration(self):
        self.surname_input.fill(fake_ru.last_name())
        self.first_name_input.fill(fake_ru.first_name())
        self.middle_name_input.fill(fake_ru.middle_name())
        birth_date = fake_ru.date_of_birth(minimum_age=25, maximum_age=30)
        birth_date_str = birth_date.strftime('%d.%m.%Y')
        self.date_of_birth_input.fill(birth_date_str)
        # self.mobile_phone_input.fill(f'9 {fake_ru.phone_number()}')
        self.mobile_phone_input.fill(f'9 {fake_ru.msisdn()}')
        self.email_input.fill(fake_ru.email())
        self.password_input.fill('123456')
        self.repeat_the_password_input.fill('123456')

    # Генерация данных для второго шага регистрации
    def generate_test_cases_second_step_of_registration(self):
        #self.pass_num_input.fill(fake_ru.passport_number())
        self.pass_num_input.fill(f'6100 {fake_ru.msisdn()}')
        self.pass_code_input.fill(fake_ru.postcode())
        self.pass_name_input.fill('МРО № 6 УФМС РОССИИ ПО АЛТАЙСКОМУ КРАЮ')
        self.pass_date_input.fill('06.07.2022')
        self.pass_birthplace_input.fill(fake_ru.city())
        self.region_input.fill('Ростовская обл')
        self.pass_birthplace_input.click()
        self.city_input.fill('г Ростов-на-Дону')
        self.pass_birthplace_input.click()
        self.street_input.fill('ул Равнинная')
        self.pass_birthplace_input.click()
        self.house_num_input.fill('д 6 ')

    # Генерация данных для третьего шага регистрации
    def generate_test_cases_third_step_of_registration(self):
        self.place_of_work_input.fill(fake_ru.company())
        self.family_income_input.click()
        self.workplace_address_input.fill(fake_ru.address())
        self.family_income_input.click()
        self.work_phone_input.fill(f'9 {fake_ru.msisdn()}')
        self.family_income_input.click()
        self.family_income_input.press("Control+A")
        self.family_income_input.press("Delete")
        self.family_income_input.press_sequentially(str(fake_ru.random_int(min=1, max=1000000)))
        self.cohabitor_phone_input.fill(f'9 {fake_ru.msisdn()}')

    # Заполнение полей на 1 шаге ригистрации и переход на 2 шаг регистрации
    def moving_to_the_second_step(self, page: Page):
        common_functions_page = CommonFunctionsPage(page)
        with allure.step('Открыть страницу первого шага регистрации'):
            self.page.goto(self.URL_FIRST_STEP)
        with allure.step('Генерируем и вставляем данные в поля'):
            common_functions_page.generate_test_cases_first_step_of_registration()
        with allure.step('Жмем кнопку "Далее"'):
            self.next_step_button.click()
        with allure.step('Проверяем что перешли на 2 шаг регистрации'):
            url = common_functions_page.URL_SECOND_STEP
            common_functions_page.page.wait_for_url(url)

    # Заполнение полей на 2 шаге ригистрации и переход на 3 шаг регистрации
    def moving_from_the_second_step_to_the_third_step(self, page: Page):
        common_functions_page = CommonFunctionsPage(page)
        common_functions_page.generate_test_cases_second_step_of_registration()
        self.next_step_button_second.click()
        url = common_functions_page.URL_THIRD_STEP
        common_functions_page.page.wait_for_url(url)

    # Заполнение полей на 3 шаге ригистрации и переход на страницу активации
    def moving_from_the_third_step_to_the_activate_step(self, page: Page):
        common_functions_page = CommonFunctionsPage(page)
        common_functions_page.generate_test_cases_third_step_of_registration()
        self.button_send_request.click()
        url = common_functions_page.URL_ACTIVATE_STEP
        common_functions_page.page.wait_for_url(url)