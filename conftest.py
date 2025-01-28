import pytest
from requests import options
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


@pytest.fixture(autouse=True)
def driver(request):
    options = Options()
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--incognito")
    options.page_load_strategy = 'eager'
    service = Service()
    driver = webdriver.Chrome(options=options, service=service)
    request.cls.driver = driver
    yield
    driver.quit()