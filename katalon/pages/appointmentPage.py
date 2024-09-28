from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime


class AppointmentPage:
    def __init__(self, driver):
        self.driver = driver
        self.facilityDropdown = (By.XPATH,"//select[@id='combo_facility']")
        self.tokyoFacility = (By.XPATH,"//option[contains(@value,'Tokyo')]")
        #self.facility = (By.XPATH,f"//option[contains(@value,'{facility_name}')]")
        self.hongkongFacility = (By.XPATH,"//option[contains(@value,'Hongkong')]")
        self.seoulFacility = (By.XPATH,"//option[contains(@value,'Seoul')]")

        self.readmissionCheckbox = (By.XPATH, "//input[@type='checkbox' and contains(@id,'readmission')]")

        self.medicareRadio = (By.XPATH, "//input[@type='radio' and contains(@value,'Medicare')]")
        self.medicaidRadio = (By.XPATH, "//input[@type='radio' and contains(@value,'Medicaid')]")
        self.noneRadio = (By.XPATH, "//input[@type='radio' and contains(@value,'None')]")


        self.dateText =  (By.XPATH, "//input[@type='text' and contains(@id,'date')]")
        self.dateMonthText =  (By.XPATH, "//div[@class='datepicker-months']//th[@class='datepicker-switch']")
        self.dateDayText =  (By.XPATH, "//div[@class='datepicker-days']//th[@class='datepicker-switch']")
        self.dateText =  (By.XPATH, "//input[@type='text' and contains(@id,'date')]")

        self.bookButton = (By.XPATH, "//button[@id='btn-book-appointment']")

    def selectFacilityAndProgram(self, facility, readmission: bool, healthcare , date):
        facility_path = (By.XPATH, f"//option[contains(@value,'{facility}')]")
        healthcare_program = (By.XPATH, f"//input[@type='radio' and contains(@value,'{healthcare}')]")
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.facilityDropdown)).click()
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(facility_path)).click()
        if readmission:
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.readmissionCheckbox)).click()
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(healthcare_program)).click()
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.dateText)).send_keys(date)
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.bookButton)).click()




