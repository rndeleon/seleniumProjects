from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.makeAppointment_button = (By.XPATH,"//a[text()='Make Appointment']")
        # self.username_textbox = (By.XPATH,"//input[@id='txt-username']")
        self.username_textbox = (By.XPATH,"//input[@id='txt-username']")
        self.username_textbox2 = (By.ID, "txt-username")
        self.password_textbox = (By.ID, "txt-password")
        self.login_button = (By.XPATH, "//button[@id='btn-login']")
        self.login_button1 = (By.CLASS_NAME, "btn btn-default")

    def open_page(self, url):
        self.driver.get(url)

    def make_appointment(self):
        # self.wait.until(EC.element_to_be_clickable(self.makeAppointment_button)).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.makeAppointment_button)
        ).click()
        # self.driver.find_element(self.makeAppointment_button).click()

    def login(self, username, password):
        # self.driver.find_element(self.makeAppointment_button).click()
        # WebDriverWait(self.driver, 5).until(self.driver.presenceOfElementLocated(self.username_textbox))
        # self.driver.find_element(self.username_textbox).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.username_textbox)).send_keys(username)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.password_textbox)).send_keys(password)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.login_button)).click()
        # self.driver.find_element(self.username_textbox).send_keys(username)
        # self.driver.find_element(self.password_textbox).send_keys(password)
        # self.driver.find_element(self.login_button).click()
    
    def logi22(self, username, password):
        self.driver.find_element(self.makeAppointment_button).click()
        # WebDriverWait(self.driver, 5).until(self.driver.presenceOfElementLocated(self.username_textbox))
        # self.driver.find_element(self.username_textbox).click()
        self.driver.find_element(*self.username_textbox).send_keys(username)
        self.driver.find_element(self.password_textbox).send_keys(password)
        self.driver.find_element(self.login_button).click()