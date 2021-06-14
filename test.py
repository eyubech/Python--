from tkinter import *
from time import strftime
from datetime import time
import tkinter as tk
root = Tk()
root.title('Masjid')
root.geometry('4800x4800')
root.configure(bg='Black')
header = Frame(height=100, width=2000, bg='#4a5658').place(x=0,y=0)

#Clock
def time():
    clock = strftime('%H:%M:%S %p')
    time_clock.config(text=clock)
    time_clock.after(1000, time)


time_clock = Label(root, font=('calibri', 45, 'bold'),background='#4a5658',foreground='white')
time_clock.pack(anchor='center')
time()

#Clock
def Date():
    clock = strftime('%a:%b:%Y')
    time_Date.config(text=clock)
    time_Date.after(1000, time)


time_Date = Label(root, font=('calibri', 25,),background='#4a5658',foreground='white')
time_Date.place(x=0,y=0)
Date()


FajrFrame = Frame(height=80, width=2000, bg='#8a979a').pack()


mainloop()