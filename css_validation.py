from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("http://w3schools.com")
driver.maximize_window()
size = driver.find_element(By.XPATH, "//*[@id=\"main\"]/div[2]/div/div[1]/a[1]").value_of_css_property("font-sze")
color = driver.find_element(By.XPATH, "//*[@id=\"main\"]/div[2]/div/div[1]/a[1]").value_of_css_property("color")

print("size :",size,"color :",color)