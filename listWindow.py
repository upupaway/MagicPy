import tkinter as tk
import tkinter.font
from CardSearch import CardSearch
import glob
import os
from tkinter import messagebox

class listWindow:

    def __init__(self, username):
        self.dirList=[]
        self.username=username
        for file in glob.glob("lists/" + self.username + r"/*.xlsx"):
            self.dirList.append(os.path.basename(file))
        if len(self.dirList) == 0:
            self.dirList = ["No lists exist, please create one"]
        self.root = tk.Toplevel()
        self.font = tkinter.font.Font(family='Beleren Small Caps', size=10)
        self.fontBig=tkinter.font.Font(family='Beleren Small Caps', size=15)



        self.root.title("Choose A List")
        self.root.geometry("355x490")
        self.background_image = tk.PhotoImage(file="cardBack.png")
        self.background_label = tk.Label(self.root, image=self.background_image)
        self.background_label.place(relwidth=1, relheight=1)

        self.frame = tk.Frame(self.root, bg='#e7e6e7')
        self.frame.place(relwidth=0.75, relheight=.07, relx=0.5, rely=0.1, anchor='n')

        self.tkDirList = tk.StringVar(self.frame)
        self.tkDirList.set(self.dirList[0])

        self.optionMenu=tk.OptionMenu(self.frame, self.tkDirList, *self.dirList)
        self.optionMenu.place(relwidth=0.7, relheight=1)

        self.button = tk.Button(self.frame, bg='#e7e6e7', text="Choose List", font=self.font,
                                command=lambda: self.buttonPress(self.username, self.tkDirList.get()))
        self.button.place(relx=.7, relheight=1, relwidth=.30)

        self.label=tk.Label(self.root, text="Welcome " + self.username +",\nChoose A List!",
                            justify='center', font=self.fontBig)
        self.label.place(relx=0.5, rely=0.35, anchor='n')

        self.frame2 = tk.Frame(self.root, bg='#e7e6e7')
        self.frame2.place(relwidth=0.75, relheight=.07, relx=0.5, rely=0.75, anchor='n')

        self.entry=tk.Entry(self.frame2, bg='#e7e6e7', font=self.font)
        self.entry.place(relheight=1, relwidth=0.6)

        self.button2 = tk.Button(self.frame2, bg='#e7e6e7', text='Make New List', font=self.font,
                                 command=lambda: self.buttonPress(username, self.entry.get()))
        self.button2.place(relx=0.6, relheight=1, relwidth=0.4)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def run(self):
        self.root.mainloop()

    def on_closing(self):
            self.root.destroy()

    def buttonPress(self, username, listname):
        if listname=='No lists exist, please create one':
            messagebox.showinfo("Failed", "You Didn't Choose A List!")
        else:
            CardSearch(username, listname)
            self.root.destroy()