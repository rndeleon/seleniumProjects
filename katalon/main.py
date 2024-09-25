from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
import time
def open_website():
    katalon = "https://katalon-demo-cura.herokuapp.com/"
    driver.get('https://katalon-demo-cura.herokuapp.com/')

    time.sleep(4)
    driver.quit()

if __name__ == '__main__':
    open_website()