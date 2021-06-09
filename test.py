from tkinter import *
from functools import partial
from tkinter import messagebox
tkWindow = Tk()
tkWindow.geometry('400x150')
tkWindow.title('Admin login')
def validateLogin(username, password):
	a = username.get()
	b = password.get()
	if a == 'admin' and b == 'admin':
		newWindow = Toplevel(tkWindow)
		newWindow.title("Profile")
		newWindow.geometry("200x200")
		Label(newWindow,text="Welcome").pack()
	else:
		messagebox.showwarning("Error", "user not found")
	return



usernameLabel = Label(tkWindow, text="User Name").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)

passwordLabel = Label(tkWindow,text="Password").grid(row=1, column=0)
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)

validateLogin = partial(validateLogin, username, password)

loginButton = Button(tkWindow, text="Login",command=validateLogin).grid(row=4, column=0)



tkWindow.mainloop()