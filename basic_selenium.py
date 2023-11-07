from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



#service = Service(executable_path='Selenium+BDD\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
options = webdriver.ChromeOptions()
#driver = webdriver.Chrome(service=service, options=options)
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

'''
IMPLICIT WAIT

driver.implicitly_wait(20)
driver.get("https://www.facebook.com/")
driver.find_element(By.ID, "email").send_keys("8861446898")
driver.find_element(By.NAME, "pass").send_keys("27NHXAK2")
driver.find_element(By.NAME, "login").click()
'''
driver.get("https://www.gmail.com")
element_email = WebDriverWait(driver, 10, 1).until(EC.element_to_be_clickable((
    By.XPATH,"/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input")))
element_email.send_keys("paulmriganka707")
time.sleep(30)

#driver.close()
driver.quit()

'''
Difference between close() and quit()
close() clsoes the current window or browser/popups where the focus is on while quit() closes the whole session
'''

