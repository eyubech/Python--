from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
driver.get("https://www.python.org")
print(driver.title)
time.sleep(10)
driver.close()