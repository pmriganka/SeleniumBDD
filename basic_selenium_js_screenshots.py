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
        self.driver.implicitly_wait(20)
    
    def js_functions(self):
        self.driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_submit_get")
        self.driver.switch_to.frame(self.driver.find_element(By.XPATH, "/html/body/div[4]/div[4]/div/div/iframe"))
        self.driver.execute_script("myFunction()")
        time.sleep(2)
        self.driver.switch_to.default_content()
        
    def capture_screenshots(self):
        self.driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_submit_get")
        self.driver.switch_to.frame(self.driver.find_element(By.XPATH, "/html/body/div[4]/div[4]/div/div/iframe"))
        def screenshot_timestamp(d, path):
            file_name = path+"screenshot_"+time.asctime().replace(":","-")+".png"
            d.save_screenshot(file_name)
        screenshot_timestamp(self.driver, "C:\\Users\\paulm5\OneDrive - Dell Technologies\\Desktop\\Development\\SeleniumBDD\\SeleniumBDD\\screenshots\\")
        
        
    def quit_driver(self):
        '''
        Difference between close() and quit()
        close() clsoes the current window or browser/popups where the focus is on while quit() closes the whole session
        '''
        #self.driver.close()
        self.driver.quit()  
        
        
if __name__ == "__main__":
    myscript = SeleniumScript()
    #myscript.js_functions()
    myscript.capture_screenshots()
    myscript.quit_driver()