import bcrypt
from database import Database
from tkinter import *
from tkinter import messagebox
import tkinter.font
import tkinter as tk
from listWindow import listWindow
import os


db = Database()
db.createTable()


class Login:

    """
        Class for Login
        @param username
        @param password
    """

    def __init__(self):
        self.smallFont = tk.font.Font(family='Beleren Small Caps', size=10)
        self.bigFont=tk.font.Font(family='Beleren Small Caps', size=30)
        self.loginWindow=tk.Toplevel()
        self.loginWindow.title("Login to Card Search")
        self.loginWindow.geometry("250x200")
        self.label=Label(self.loginWindow, text="Log In", font=self.bigFont)
        self.label.place(x=65, y=10)
        self.usernameE = Entry(self.loginWindow, justify='center', width=15, font=self.smallFont)
        self.usernameE.place(x=95, y=80)
        self.userLabel=Label(self.loginWindow, text="username:", font=self.smallFont)
        self.userLabel.place(x=35, y=80)
        self.passwordE = Entry(self.loginWindow, show="*", justify='center', width=15, font=self.smallFont)
        self.passwordE.place(x=95, y=120)
        self.passLabel=Label(self.loginWindow, text="password:", font=self.smallFont)
        self.passLabel.place(x=35, y=120)
        self.submit = Button(self.loginWindow, text="Submit", pady=5, padx=20, font=self.smallFont, command=self.validate)
        self.submit.place(x=85, y=150)


    def validate(self,):
        self.username=self.usernameE.get()
        self.password=self.passwordE.get()
        data = (self.username,)
        inputData = (self.username,self.password)
        try:
            if (db.validateData(data, inputData)):
                messagebox.showinfo("Successful", "Logged In Successfully")
                self.loginWindow.destroy()
                cardListTk=listWindow(self.username)
                cardListTk.run()
            else:
                messagebox.showerror("Error", "Wrong Credentials")
        except IndexError:
            messagebox.showerror("Error", "Wrong Credentials")

    def run(self):
        self.loginWindow.mainloop()

class Register:

    """
        Class for Register
        @param username
        @param password
    """

    def __init__(self):
        self.smallFont = tk.font.Font(family='Beleren Small Caps', size=10)
        self.bigFont=tk.font.Font(family='Beleren Small Caps', size=30)
        self.registerWindow=tk.Toplevel()
        self.registerWindow.title("Registration")
        self.registerWindow.geometry("250x200")
        self.label=Label(self.registerWindow, text="Register", font=self.bigFont)
        self.label.place(x=40, y=10)
        self.usernameE = Entry(self.registerWindow,  width=15, font=self.smallFont, justify='center')
        self.usernameE.place(x=95, y=80)
        self.userLabel=Label(self.registerWindow, text="username:", font=self.smallFont)
        self.userLabel.place(x=35, y=80)
        self.passwordE = Entry(self.registerWindow, show="*", width=15, font=self.smallFont, justify='center')
        self.passwordE.place(x=95, y=120)
        self.passLabel = Label(self.registerWindow, text="password:", font=self.smallFont)
        self.passLabel.place(x=35, y=120)
        self.submit = Button(self.registerWindow, text="Submit", pady=5, padx=20, command=self.add)
        self.submit.place(x=85, y=150)


    def run(self):
        self.registerWindow.mainloop()

    def add(self):
        self.username=self.usernameE.get()
        self.password=self.passwordE.get()
        self.salt=bcrypt.gensalt()
        self.hashed=bcrypt.hashpw(self.password.encode(), self.salt)
        data = (self.username,)

        result = db.searchData(data)

        if result != 0:
            data = (self.username, self.hashed, self.salt)
            db.insertData(data)
            messagebox.showinfo("Successful", "Registered Your Account")
            os.mkdir('lists/' + self.username)
            self.registerWindow.destroy()
        else:
            messagebox.showerror("Cannot Execute", "User Already Exists")
