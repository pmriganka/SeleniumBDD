from basic_selenium import SeleniumScript
from basic_selenium import *
from selenium.webdriver.chrome.options import Options

class Sub_BO_SeleniumScript(SeleniumScript):

    def handling_push_notifications(self):
        chrome_options = Options()
        prefs = {"profile.default_content_setting_values.notifications" : 2}
        chrome_options.add_experimental_option("prefs", prefs)
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options = chrome_options)
        self.driver.maximize_window()
        self.driver.get("https://www.redbus.in/")
        
        
    def full_page_screenshot(self):
        chrome_options = Options()
        prefs = {"profile.default_content_setting_values.notifications" : 2}
        chrome_options.add_experimental_option("prefs", prefs)
        chrome_options.headless = True
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options = chrome_options)
        self.driver.get("https://www.way2automation.com/")
        func = lambda X: self.driver.execute_script("return document.body.parentNode.scroll" + X )
        self.driver.set_window_size(func('Width'), func('Height'))
        self.driver.find_element(By.TAG_NAME , "body").screenshot("C:\\Users\\paulm5\\OneDrive - Dell Technologies\\Desktop\\Development\\SeleniumBDD\\SeleniumBDD\\screenshots\\fullpage.png")
        
        

if __name__ == "__main__":
    myscript = Sub_BO_SeleniumScript()
    #myscript.handling_push_notifications()
    myscript.full_page_screenshot()
    myscript.quit_driver()