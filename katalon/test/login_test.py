import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from seleniumProjects.katalon.pages.LoginPage import LoginPage
from seleniumProjects.katalon.pages.appointmentPage import AppointmentPage


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    yield driver
    driver.close()
    driver.quit()

def login(driver, username, password):
    """Helper function to perform login."""
    login_page = LoginPage(driver)
    login_page.open_page('https://katalon-demo-cura.herokuapp.com/')
    login_page.make_appointment()
    login_page.login(username, password)
    time.sleep(5)

def test_login(driver):
    login(driver, "John Doe", "ThisIsNotAPassword")

def test_set_facility(driver):
    appointment_page = AppointmentPage(driver)
    login(driver, "John Doe", "ThisIsNotAPassword")
    appointment_page.selectFacilityAndProgram("Hongkong",True)
    time.sleep(5)


