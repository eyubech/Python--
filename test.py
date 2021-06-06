from tkinter import *
from tkinter import ttk
win = Tk()

button = ttk.Button(win, text='Click me')
button.pack()

def callback():
    print('python')

button.config(command = callback)

logo = PhotoImage(file='1.png')

button.config(image=logo)
print('first test')
print('test from github')
win.mainloop()
