from tkinter import *
from login import Login, Register
import tkinter as tk
import tkinter.font
import os


class MainWindow:
    def __init__(self):


        self.app = tk.Tk()
        self.smallFont = tk.font.Font(family='Beleren Small Caps', size=10)
        self.bigFont = tk.font.Font(family='Beleren Small Caps', size=30)
        self.app.title("MagicPy")
        self.app.geometry("250x200")
        self.label = Label(self.app, text="MagicPy", font=self.bigFont)
        self.label.place(x=40, y=10)
        self.login = Button(self.app, text="Login",
                            pady=5, padx=29, command=login, font=self.smallFont)
        self.login.place(x=70, y=70)
        self.register = Button(self.app, text="Register",
                               pady=5, padx=20, command=register, font=self.smallFont)
        self.register.place(x=70, y=120)
        if os.path.exists('lists'):
            pass
        else: os.mkdir('lists')

    def run(self):

        self.app.mainloop()


def login():
    loginTk = Login()
    loginTk.run()


def register():
    registerTk = Register()
    registerTk.run()


app = MainWindow()
app.run()