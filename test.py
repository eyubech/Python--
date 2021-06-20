from tkinter import *
from time import strftime
from datetime import time
import tkinter as tk
import csv
root = Tk()
root.title('Masjid')
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

#First Frame
Trait= Frame(height=2, width=2000, bg='black').pack()
FirstFrame = Frame(height=80, width=2000, bg='#8a979a').pack()
Prayer = Label(root, text='PRAYER',font=('calibri', 35),foreground='black', background='#8a979a')
Prayer.place(x=40,y=85)
Beginning = Label(root, text='BEGINNING',font=('calibri', 35),foreground='black', background='#8a979a')
Beginning.place(x=800,y=85)
Jamaat = Label(root, text='JAMAAT',font=('calibri', 35),foreground='black', background='#8a979a')
Jamaat.place(x=1600,y=85)



#Fram 2
Trait2= Frame(height=2, width=2000, bg='black').pack()
Frame2 = Frame(height=100, width=2000, bg='#8a979a').pack()
fa = Label(root, text='FAJAR',font=('calibri', 25),foreground='black', background='#8a979a').place(x=40, y =210)
ff = Label(root, text='فجر',font=('calibri', 25),foreground='black', background='#8a979a').place(x=40, y =160)

#Fram 3
Trait3= Frame(height=2, width=2000, bg='black').pack()
Frame3 = Frame(height=120, width=2000, bg='#8a979a').pack()

#Fram 4
Trait4= Frame(height=2, width=2000, bg='black').pack()
Frame4 = Frame(height=100, width=2000, bg='#8a979a').pack()

#Fram 5
Trait5= Frame(height=2, width=2000, bg='black').pack()
Frame5 = Frame(height=100, width=2000, bg='#8a979a').pack()



#Fram 6
Trait6= Frame(height=2, width=2000, bg='black').pack()
Frame6 = Frame(height=100, width=2000, bg='#8a979a').pack()



#Fram 7
Trait7= Frame(height=2, width=2000, bg='black').pack()
Frame7 = Frame(height=100, width=2000, bg='#8a979a').pack()


#Fram 8
Trait8= Frame(height=2, width=2000, bg='black').pack()
Frame8 = Frame(height=100, width=2000, bg='#8a979a').pack()

#Fram 9
Trait9= Frame(height=2, width=2000, bg='black').pack()
Frame9 = Frame(height=120, width=2000, bg='#4a5658').pack()










































































mainloop()