import tkinter as tk
import pytube
root = tk.Tk()
root.title('Youtube downloader')
root.geometry('500x100')

lien_var = tk.StringVar()
def url():
    lien = lien_var.get()
    youtube = pytube.YouTube(lien)
    video = youtube.streams.first()
    video.download()
    lien_var.set("")


title = tk.Label(root, text='youtube downloader',font=('Helvatical bold',30,'bold')).pack()
ent = tk.Entry(root, width="50", textvariable = lien_var).pack()
down = tk.Button(root, text='Download',command=url).pack()






root.mainloop()