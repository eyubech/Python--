from tkinter import *
from tkinter import ttk

root = Tk()
Progressbar = ttk.Progressbar(root, orient = HORIZONTAL, length = 300)
Progressbar.pack()

Progressbar.config(maximum=20, value=3)
Progressbar.start()

value = DoubleVar()
Progressbar.config(variable = value)

scale = ttk.Scale(root, orient = HORIZONTAL
                  ,length = 400
                  ,variable=value
                  ,from_=0.0 ,to =20)
scale.pack()
scale.set(3)
root.mainloop()






root.mainloop()