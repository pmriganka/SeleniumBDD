from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import time


class SeleniumScript:

    def __init__(self):
        #service = Service(executable_path='Selenium+BDD\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
        #options = webdriver.ChromeOptions()
        #driver = webdriver.Chrome(service=service, options=options)
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
    
    def implicit_wait(self):
        self.driver.implicitly_wait(20)
        self.driver.get("https://www.facebook.com/")
        self.driver.find_element(By.ID, "email").send_keys("8861446898")
        self.driver.find_element(By.NAME, "pass").send_keys("27NHXAK2")
        self.driver.find_element(By.NAME, "login").click()


    def explicit_wait(self):
        self.driver.get("https://www.gmail.com")
        element_email = WebDriverWait(self.driver, 10, 1).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input")))
        element_email.send_keys("paulmriganka707")
        time.sleep(5)

    def quit_driver(self):
        '''
        Difference between close() and quit()
        close() clsoes the current window or browser/popups where the focus is on while quit() closes the whole session
        '''
        #self.driver.close()
        self.driver.quit()
    
    def dropdown(self):
        self.driver.implicitly_wait(50)
        self.driver.get("https://wikipedia.org")
        dpdwn_element = self.driver.find_element(By.ID, "searchLanguage")
        select = Select(dpdwn_element)
        time.sleep(2)
        select.select_by_value("hi")
        time.sleep(2)
        #Finding all the elements and number of elements
        selected_option_list = select.options
        for option in selected_option_list:
            print(option.text,"language is : ",option.get_attribute("lang"))
        print("Number of items", len(selected_option_list))


    def finding_links(self):
        self.driver.implicitly_wait(20)
        self.driver.get("https://wikipedia.org")
        whole_section = self.driver.find_element(By.XPATH, "//*[@id=\"www-wikipedia-org\"]/div[10]/div[3]")
        links = whole_section.find_elements(By.TAG_NAME, "a")
        print("Total number of links : ",len(links) )
        print("First link is : ", links.__getitem__(0).text)



if __name__ == "__main__":
    myscript = SeleniumScript()
    #myscript.explicit_wait()
    #myscript.dropdown()
    myscript.finding_links()
    myscript.quit_driver()





