from selenium import webdriver
web = webdriver.Chrome()
web.set_window_position(2000,550)
web.get("https://www.amazon.com/")

y = web.find_element_by_id("twotabsearchtextbox")
y.send_keys("Iphone")

w = web.find_element_by_id("nav-search-submit-button")
w.click()

ip = web.find_element_by_class_name("s-image")
ip.click()

cart = web.find_element_by_id("add-to-cart-button")
cart.click()