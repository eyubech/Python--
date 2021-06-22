from tkinter import *
import tkinter as tk
from selenium import webdriver
from tkinter import messagebox
import time
root = tk.Tk()
root.title('Egybest Downloader')
root.geometry('500x150')

lien_var = tk.StringVar()
#fonction
def url():
    film = lien_var.get()
    url = 'https://back.egybest.co/movies/2020'
    driver = webdriver.Chrome()
    driver.get(url)
    textbox = driver.find_element_by_xpath('//*[@id="head"]/div/div[2]/form/input[2]')
    textbox.click()
    time.sleep(1)
    driver.switch_to.window(driver.window_handles[0])
    textbox.click()
    time.sleep(1)
    textbox.send_keys(film)
    time.sleep(1)
    ign = driver.find_element_by_class_name('NotificationIgnore')
    ign.click()
    search_b = driver.find_element_by_class_name('slist')
    search_b.click()
    film = driver.find_element_by_xpath('//*[@id="movies"]/a[3]/img')
    film.click()
    first_button = driver.find_element_by_xpath('//*[@id="mainLoad"]/div[1]/div[2]/div[1]/a')
    first_button.click()
    sec_button = driver.find_element_by_xpath('//*[@id="watch_dl"]/table/tbody/tr[1]/td[4]/a[1]')
    sec_button.click()
    dow = driver.find_element_by_xpath('/html/body/div[1]/div/p/a[1]')
    dow.click()
    time.sleep(2)
    driver.close()
    dow.click()
    time.sleep(2)
    driver.close()
    lien_var.set("")
    tk.messagebox.showinfo(title='Download', message='Done')
    return film


title = tk.Label(root, text='Egybest downloader',font=('Helvatical',30,'bold')).pack()
t2 = tk.Label(root, text='Enter your film',font=('Helvatical',15,'bold')).pack()
entry = tk.Entry(root, width='50', textvariable=lien_var).pack()

btt = tk.Button(root,text='Download',command=url).pack()


root.mainloop()