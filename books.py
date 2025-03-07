import sqlite3 as sql
import tkinter as tk
import tkinter.font as tkFont


class bookFrame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.titlefont = tkFont.Font(family="Arial", size=20, slant="italic")
        self.mainfont = tkFont.Font(family="Courier", size=18)
        l1 = tk.Label(self,text="Choose Books", font=self.titlefont)
        l1.grid(row=0,column=0, sticky="W",columnspan=6)

        l2 = tk.Label(self,text="Available books:", font=self.mainfont)
        l2.grid(row=2,column=1, sticky="W")

        self.rowconfigure(1,minsize=100)
        self.booklist = tk.Listbox(self,width=30, height=20)
        self.booklist.grid(row=3, column=1)

        l2 = tk.Label(self,text="Your books:", font=self.mainfont)
        l2.grid(row=2,column=5, sticky="W")
        
        self.ownBooks = tk.Listbox(self,width=30)
        self.ownBooks.grid(row=3, column=5)

        self.rowconfigure(1,minsize=100)
        self.columnconfigure(3,weight=50)
        self.columnconfigure(0,weight=50)
        self.columnconfigure(7,weight=50)

    def loadUp(self):
        # put code in here to be run when this frame is displayed
        
        # read in database and put in the listbox
        results = self.parent.cursor.execute("SELECT * FROM books")
        results = results.fetchall()
        for i in results:
            self.booklist.insert(tk.END, i[1])
        pass
