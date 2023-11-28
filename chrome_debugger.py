from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options



#Go to chrome.exe Location on command prompt
#C:\Users\paulm5\AppData\Local\Google\Chrome\Application
#Create a folder on C drive - C:\chromedata
#issue "chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\chromedata"
#Include the debugger options in chrome options

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1: 9222")
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
driver.get("http://gmail.com")
driver.maximize_window()
driver.find_element(By.XPATH, "/html/body/header/div/div/div/a[2]").click()
driver.find_element(By.XPATH, "//*[@id=\"identifierId\"]").send_keys("paulmriganka707")
driver.find_element(By.XPATH, "//*[@id=\"identifierNext\"]/div/button/span").click()