from tkinter import *
from tkinter import ttk

window = Tk()

label = ttk.Label(window, text='hello world')
label.pack()
label.config(foreground='silver', background='brown')
label.config(font=('Aria',20,'bold'))

label.config(wraplength=150)
label.config(justify=CENTER)


logo = PhotoImage(file='1.png')
label.config(image=logo)
label.config(compound='center')
label.config(compound='right')



window.mainloop()