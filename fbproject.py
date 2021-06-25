import tkinter as tk
from tkinter import messagebox
import instaloader

root = tk.Tk()
root.title('VDownloader')
root.geometry('500x150')

lien_var = tk.StringVar()
#fonction
def url():
    # to get url from Entry
    user = lien_var.get()
    ig = instaloader.Instaloader()
    ig.download_profile(user, profile_pic_only=True)
    lien_var.set("")
    tk.messagebox.showinfo(title='Download', message='Done')

title = tk.Label(root, text='youtube downloader',font=('Helvatical',30,'bold')).pack()

entry = tk.Entry(root, width='50', textvariable=lien_var).pack()

btt = tk.Button(root,text='Download',command=url).pack()


root.mainloop()