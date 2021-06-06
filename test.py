from tkinter import *
from tkinter import ttk

root = Tk()
combo = ttk.Combobox(root)
combo.pack()
combo.config(values=('jan', 'feb', 'mar','apr','may','jun'))

print('feb')
combo.set('apr')

spin = Spinbox(root, from_=1990, to=2021).pack()
print(2000)

root.mainloop()