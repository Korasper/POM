from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):

    PAGE_URL = "https://www.freeconferencecall.com/global/pl/login"

    LOGIN_FIELD = ("xpath", "(//input[@name='email'])[1]")
    PASSWORD_FIELD = ("xpath", "(//input[@type='password'])[1]")

    def enter_login(self, login):
        login_field = self.driver.find_element(*self.LOGIN_FIELD)
        login_field.send_keys(login)

    def enter_password(self, password):
        password_field = self.driver.find_element(*self.PASSWORD_FIELD)
        password_field.send_keys(password)