from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

chrome_option=Options()
chrome_option.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=chrome_option)
#Launch browser and hit URL
driver.get("https://brightinfo.in/login.html")

#Maximize window
driver.maximize_window()

driver.get("https://www.facebook.com/")

#Maximize window
driver.maximize_window()

driver.back()
time.sleep(10)

driver.forward()
time.sleep(10)

driver.refresh()

print(driver.current_url)










