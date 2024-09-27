import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from seleniumProjects.katalon.pages.LoginPage import LoginPage


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    yield driver
    driver.close()
    driver.quit()


def test_login(driver):
    login_page = LoginPage(driver)
    login_page.open_page('https://katalon-demo-cura.herokuapp.com/')
    login_page.make_appointment()
    login_page.login("John Doe","ThisIsNotAPassword")
    time.sleep(5)

def test_login

