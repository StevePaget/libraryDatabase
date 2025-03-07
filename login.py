import sqlite3 as sql
import tkinter as tk
import tkinter.font as tkFont


class loginFrame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.parent = parent
        # The parent is a link to the main App. If you need to remember values "globally",
        # you should store them in self.parent
        # 
        # for example:
        self.parent.loggedInUser = None
        
        self.titlefont = tkFont.Font(family="Arial", size=20, slant="italic")
        self.mainfont = tkFont.Font(family="Courier", size=18)
        l1 = tk.Label(self,text="Welcome to the Library", font=self.titlefont)
        l1.grid(row=0,column=0)

        l2 = tk.Label(self, text="Username:", font=self.mainfont)
        l2.grid(row=2,column=0)
        self.userbox = tk.Entry(self, width=30)
        self.userbox.grid(row=2, column=1)

        l3 = tk.Label(self, text="Password:", font=self.mainfont)
        l3.grid(row=3,column=0)
        self.passbox = tk.Entry(self, width=30,show="*")
        self.passbox.grid(row=3, column=1)

        s = tk.Button(self,text="Submit", command=self.submit)
        s.grid(row=4,column=0, columnspan=2,sticky="EW")

        # Add code here to display a login screen
        self.errorLabel = tk.Label(self,text="", fg="red", font=self.titlefont)
        self.errorLabel.grid(row=5, column=0, columnspan=2, sticky="EW")
        
        self.rowconfigure(1,minsize=100)

        
        # Do not run any actual code in __init__
        # Because this will be run as soon as the program loads

    def loadUp(self):
        # put code in here to be run when this frame is displayed
        self.userbox.focus()
        self.parent.bind("<Return>", self.submit)


    def submit(self, e=None):
        # check the contents of the entry boxes and see if they have logged in correctly
        # if so, set self.parent.loggedInUser
        self.parent.loggedInUser = None

        username = self.userbox.get()
        password = self.passbox.get()
        results = self.parent.cursor.execute("SELECT * from users WHERE username = ? and password = ?", (username, password))
        results = results.fetchall()
        if True: #    len(results) == 1:
            # OK login
            # Then switch frames
            self.parent.switchFrame("books")
            self.parent.loggedInUser = "bob54" # username
        else:
            # bad login
            self.errorLabel.configure(text="Wrong username or password")
