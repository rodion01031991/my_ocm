from playwright.sync_api import Page

class LoginPage(Page):
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator('#loginform-username')
        self.password_input = page.locator('#loginform-password')
        self.login_button = page.locator('#idx_login')
        self.error_message = page.locator('.error-page-field')


    def open_login_page(self):
        self.page.goto('https://rc.dev.oneclickmoney.ru/#signin')


    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()


    def get_error_message(self):
        return self.error_message.inner_text()