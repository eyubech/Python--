from tkinter import *
from tkinter import ttk

root = Tk()
root.title("frame")
frame = ttk.Frame(root)
frame.pack()

frame.config(height=200, width=400)
frame.config(relief = SUNKEN)

ttk.Button(frame, text='Frame').pack()
frame.config(padding=(50, 25))
ttk.LabelFrame(root, height = 200, width = 400, text = 'My frame').pack()


root.mainloop()