from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('https://back.egybest.co/vs-mirror/vidstream.kim/f/bELYTjfwIA/?vclid=cfaae7e819d833ca9b313a6c290f4afd552480f250f23806313cc2bdIUUUclNQUcUVUcAPaMKroMBnDcVcUcKliUcUVUcMLxiHUmFMMcMyrLOUtcSxcVcUcItMHcUVUcLWYzMiMnIdStUVMfaAMsUUcUR')
time.sleep(5)
down2 = driver.find_element_by_xpath('/html/body/div[1]/div/p/a[1]/i').click()
time.sleep(3)
driver.switch_to.window(driver.window_handles[0])
time.sleep(2)
down3 = driver.find_element_by_xpath('/html/body/div[1]/div/p/a[1]/i').click()

