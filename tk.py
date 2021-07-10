from tkinter import *
import tkinter as tk
from selenium import webdriver
from tkinter import messagebox
from selenium.webdriver.common.keys import Keys
import time
root = tk.Tk()
root.title('Egybest Downloader')
root.geometry('500x150')
lien_var = tk.StringVar()
def url():
    film = lien_var.get()
    url = 'https://back.egybest.co/movies/2020'
    driver = webdriver.Chrome()
    driver.get(url)
    textbox = driver.find_element_by_xpath('//*[@id="head"]/div/div[2]/form/input[2]')
    textbox.click()
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(1)
    textbox.click()
    time.sleep(1)
    textbox.send_keys(film)
    time.sleep(3)
    ign = driver.find_element_by_class_name('NotificationIgnore')
    ign.click()
    textbox.send_keys(Keys.DOWN)
    textbox.send_keys(Keys.ENTER)
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, 13)")
    down1 = driver.find_element_by_xpath('//*[@id="watch_dl"]/table/tbody/tr[2]/td[4]/a[1]')
    down1.click()
    time.sleep(5)
    down2 = driver.find_element_by_name('a.bigbutton._reload')
    down2.click()
    driver.switch_to.window(driver.window_handles[1])
    down2.click()
    lien_var.set("")
    tk.messagebox.showinfo(title='Download', message='Enjoy the film \n Insta : ayoubech__')
    return film
title = tk.Label(root, text='Egybest downloader',font=('Helvatical',30,'bold')).pack()
t2 = tk.Label(root, text='Enter your film',font=('Helvatical',15,'bold')).pack()
entry = tk.Entry(root, width='50', textvariable=lien_var).pack()
btt = tk.Button(root,text='Download',command=url).pack()
root.mainloop()