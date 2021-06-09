from tkinter import *
from tkinter import ttk

root = Tk()
note = ttk.Notebook(root)

t1 = Frame(note)
t2 = Frame(note)
t3 = Frame(note)
ttk.Button(t1, text='Exit', command=root.destroy).pack(padx=100, pady=100)
ttk.Button(t2, text='Exit', command=root.destroy).pack(padx=100, pady=100)
ttk.Button(t3, text='Exit', command=root.destroy).pack(padx=100, pady=100)


note.add(t1, text='Tab One')
note.add(t2, text='Tab Two')
note.add(t3, text='Tab Three')

note.pack()


root.mainloop()