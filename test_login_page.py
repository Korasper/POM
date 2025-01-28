import time

from pages.login_page import LoginPage


class TestLoginPage:

    def setup_method(self):
        self.login_page = LoginPage(self.driver)


    def test_login_in_account(self):
        self.login_page.open()
        self.login_page.enter_login("qweew321")
        self.login_page.enter_password("ds3423sdas")
        time.sleep(3)


