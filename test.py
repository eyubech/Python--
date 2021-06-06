from tkinter import *
win = Tk()
win.geometry('200x200')

def show_entey():
    print("Name:%s\npassword:%s"%(e1.get(), e2.get()))

e1 = Entry(win)
e2 = Entry(win)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

Label(win, text='name').grid(row=0)
Label(win, text='password').grid(row=1)

Button(win, text='quit', command=win.quit).grid(row=2, column=0)
Button(win, text='show', command=show_entey).grid(row=2, column=1)

mainloop()