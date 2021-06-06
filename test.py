from tkinter import *
from tkinter import ttk

def resize(ev=None):
    label.configure(font='Aria -%d bold' %scale.get())

root = Tk()
root.geometry('500x500')

label = ttk.Label(root, text='hello tkinter')
label.pack(fill = 'y', expand=1)
label.config(foreground='silver', background='brown')

scale = ttk.Scale(root, from_=10,to=70,command=resize)
scale.set(20)
scale.pack()

quit = ttk.Button(root,text='quit', command=root.quit)
quit.pack()




root.mainloop()