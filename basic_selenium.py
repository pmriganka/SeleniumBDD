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
        
    def mouse_over_menu(self):
        #selenium.driver.common.action.chains
        self.driver.get("https://www.way2automation.com/")
        menu = self.driver.find_element(By.XPATH, "//*[@id=\"menu-item-27617\"]")
        actions = ActionChains(self.driver)
        actions.move_to_element(menu).perform()
        self.driver.find_element(By.XPATH, "//*[@id=\"menu-item-27618\"]").click()

    def handle_sliders(self):
        #selenium.driver.common.action.chains
        self.driver.get("https://www.globalsqa.com/demo-site/sliders/#Color%20Picker")
        #iframe_size = self.driver.find_elements(By.TAG_NAME, "iframe")
        self.driver.switch_to.frame(self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div[1]/p/iframe"))
        mainslider = self.driver.find_element(By.XPATH, "/html/body/div[1]/div")
        location = mainslider.location
        size = mainslider.size
        height, breadth = size['height'], size['width']
        slider = self.driver.find_element(By.XPATH, "/html/body/div[1]/span")
        actions = ActionChains(self.driver)
        #drag the locater to the middle
        actions.drag_and_drop_by_offset(slider, 0, height/3).perform()
        time.sleep(3)
        print("Heigth = ", height, "breadth= ",breadth)
              
        
    def mresize_element(self):
        #selenium.driver.common.action.chains
        self.driver.get("https://jqueryui.com/slider/")
        mainslider = self.driver.find_element(By.CSS_SELECTOR, "#slider")
        resizable = self.driver.find_element(By.XPATH, "//*[@id=\"resizable\"]/div[3]") 
        ActionChains(self.driver).drag_and_drop_by_offset(resizable, 400, 400).perform()
        
    def drag_and_drop(self):
        #selenium.driver.common.action.chains
        self.driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
        new_iframe = self.driver.switch_to.frame(self.driver.find_element(By.XPATH, "//*[@id=\"post-2669\"]/div[2]/div/div/div[1]/p/iframe"))
        dragable  = self.driver.find_element(By.XPATH, "//*[@id=\"gallery\"]/li[3]/img")
        dropable = self.driver.find_element(By.XPATH, "//*[@id=\"trash\"]")
        ActionChains(self.driver).drag_and_drop(dragable, dropable).perform()
        time.sleep(2)
        
    def right_click(self):
        #selenium.driver.common.action.chains
        self.driver.get("https://jqueryui.com/droppable/")
        img  = self.driver.find_element(By.XPATH, "//*[@id=\"droppable\"]") 
        ActionChains(self.driver).context_click(img).perform()


    def alerts(self):
        self.driver.get("https://mail.rediff.com/cgi-bin/login.cgi")
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div[2]/form/div[1]/div[2]/div[2]/div[2]/div/input[2]").click()
        time.sleep(3)
        alert = Alert(self.driver)
        print(alert.text)
        alert.accept()
        time.sleep(3)

    def popups(self):
        pass


if __name__ == "__main__":
    myscript = SeleniumScript()
    #myscript.explicit_wait()
    #myscript.dropdown()
    #myscript.finding_links()
    #myscript.mouse_over_menu()
    #myscript.handle_sliders()
    #myscript.drag_and_drop()
    #myscript.alerts()
    myscript.popups()
    myscript.quit_driver()





