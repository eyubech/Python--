from selenium import webdriver
import time
product = input('Enter product name')
print('Created by ayoub ech-chetyouy')
web = webdriver.Chrome()
web.set_window_position(2000,550)
web.get("https://www.amazon.com/")
y = web.find_element_by_id("twotabsearchtextbox")
y.send_keys(product)
w = web.find_element_by_id("nav-search-submit-button")
w.click()
ip = web.find_element_by_class_name("s-image")
ip.click()
try:
    cart = web.find_element_by_id("add-to-cart-button")
    cart.click()
except:
    while True:
        time.sleep(2)
        web.refresh()