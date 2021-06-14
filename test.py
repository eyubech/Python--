from tkinter import *
from functools import partial
from tkinter import *
from time import strftime
import tkinter as tk
root = Tk()
root.title('Masjid')
root.geometry('4800x4800')
root.configure(bg='Black')
header = Frame(height=100, width=2000, bg='grey').place(x=0,y=0)

#Clock
def time():
    clock = strftime('%A:%M:%S %p')
    time_clock.config(text=clock)
    time_clock.after(1000, time)
time_clock = Label(root, font=('calibri', 40, 'bold'),background='grey',foreground='white')
time_clock.pack()
time()

#Date
def Date():
    date = strftime('%A:%M:%S %p')
    time_clock.config(text=date)
    time_clock.after(1000, time)
time_date = Label(root, font=('calibri', 30, 'bold'),background='grey',foreground='white')
time_date.pack()
time()




mainloop()