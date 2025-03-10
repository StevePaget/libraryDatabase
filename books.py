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
        self.booklist.grid(row=3, column=1, rowspan=3)

        l2 = tk.Label(self,text="Your books:", font=self.mainfont)
        l2.grid(row=2,column=5, sticky="W")
        
        self.ownbookslist = tk.Listbox(self,width=30)
        self.ownbookslist.grid(row=3, column=5)

        addButton = tk.Button(self,text="Add >>", command = self.add)
        addButton.grid(row=3,column=3)
        delButton = tk.Button(self,text="<< Del",command = self.remove)
        delButton.grid(row=4,column=3)

        self.rowconfigure(1,minsize=100)
        self.columnconfigure(3,weight=50)
        self.columnconfigure(0,weight=50)
        self.columnconfigure(7,weight=50)

    def loadUp(self):
        # put code in here to be run when this frame is displayed
        # read in database and put in the listbox
        self.ownbookslist.delete(0,tk.END)
        self.booklist.delete(0,tk.END)
        results = self.parent.cursor.execute("SELECT * FROM books where id not in (SELECT id from owned)")
        self.bookData = results.fetchall()
        for row in self.bookData:
            self.booklist.insert(tk.END, row[1])

        results = self.parent.cursor.execute("SELECT books.title, books.id FROM books, owned where books.id = owned.id and owned.username = ?", (self.parent.loggedInUser,))
        self.ownedbooks = results.fetchall()
        for row in self.ownedbooks:
            self.ownbookslist.insert(tk.END, row[0])
        pass


    def add(self):
        # find the book that is selected in the booklist
        selected = self.booklist.curselection()[0]
        bookID = self.bookData[selected][0]
        # add it to the owned table
        self.parent.cursor.execute("INSERT INTO owned VALUES (?,?)", (self.parent.loggedInUser, bookID))
        self.parent.db.commit()
        # refresh the owned list
        self.loadUp()

    def remove(self):
        # find the book that is selected in the ownbookslist
        selected = self.ownbookslist.curselection()[0]
        bookID = self.ownedbooks[selected][1]
        # remove it from the owned table
        self.parent.cursor.execute("DELETE FROM owned WHERE id = ? and username = ?", (bookID,self.parent.loggedInUser))
        self.parent.db.commit()
        # refresh the owned list
        self.loadUp()