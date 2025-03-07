import sqlite3 as sql
import tkinter as tk
import tkinter.font as tkFont
from login import loginFrame
from books import bookFrame


class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry("900x700+100+100")
        self.title("Library Database Demo")

        # This dictionary stores all the frames in the database,which have been imported from separate files
        self.frames = {"login":loginFrame(self), "books":bookFrame(self)}

        self.db = sql.connect("library.db")
        self.cursor = self.db.cursor()
        
        self.rowconfigure(0, weight=100)
        self.columnconfigure(0, weight=100)

        self.testDatabase()
        self.switchFrame("login")
        self.mainloop()

    def testDatabase(self):
        # This just prints out the contents of the database
        results = self.cursor.execute("SELECT * from users")
        results = results.fetchall()
        for line in results:
            print(", ".join(line))
        results = self.cursor.execute("SELECT * from books")
        results = results.fetchall()
        for line in results:
            print(line)

    def switchFrame(self,frame):
        # this function switches the currently visible frame.
        # You send is a string like "books" or "login" and it
        #   looks in self.frames to see if it exists

        # it puts that frame on the grid, and removes all others
        valid = False
        for f in self.frames:
            if f == frame:
                self.frames[f].grid(row=0, column=0,sticky="NSEW")
                self.frames[f].loadUp()
                valid=True
            else:
                self.frames[f].grid_forget()
        if not valid:
            e1 = tk.Label(self,text=f"Error: no such frame as '{frame}'", fg="red", font = tkFont.Font(family="Arial", size=30))
            e1.grid(row=0,column=0, sticky="NSEW")

main = App()

