from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    HOST_BUTTON_LOCATOR = ("xpath", "(//button[@type='submit'])[2]")
    JOIN_BUTTON_LOCATOR = ("xpath", "(//button[text()='Join']")

    def __init__(self,driver):
        self.driver: WebDriver = driver

    def open(self):
        self.driver.get(self.PAGE_URL)

    def join(self):
        self.driver.find_element(*self.JOIN_BUTTON_LOCATOR).click()

    def host(self):
        self.driver.find_element(*self.HOST_BUTTON_LOCATOR).click()




