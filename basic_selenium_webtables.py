from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
import time


class SeleniumScript:

    def __init__(self):
        #service = Service(executable_path='Selenium+BDD\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
        #options = webdriver.ChromeOptions()
        #driver = webdriver.Chrome(service=service, options=options)
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
    
    def working_with_table(self):
        self.driver.get("https://www.espncricinfo.com/series/icc-cricket-world-cup-2023-24-1367856/points-table-standings")
        first_element = self.driver.find_element(By.XPATH, "//*[@id=\"main-container\"]/div[3]/div[4]/div/div/table/tbody/tr[1]/td[1]")
        print(first_element.text)
            
        

if __name__ == "__main__":
    myscript = SeleniumScript()
    myscript.working_with_table()
    myscript.quit_driver()