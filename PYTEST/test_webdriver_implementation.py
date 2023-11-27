from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import pytest



def setup_function():
    global driver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("http://facebook.com")
    driver.maximize_window()
    driver.implicitly_wait(5)
    
def teardown_function():
    driver.quit()
    
def get_data():
    return [
        ("sgdfhasdghfg@gmail.com", "sadfsdaf"),
        ("sgdfherfl.com", "saeqwdaf")
    ]

@pytest.mark.parametrize("username, password", get_data())
def test_dologin(username , password):
    driver.find_element(By.ID, "email").send_keys(username)
    driver.find_element(By.ID, "pass").send_keys(password)

#To generate html report    
#python -m pytest test_webdriver_implementation.py -s -v --html=testreports.html
#report will be generated in the pytest folder