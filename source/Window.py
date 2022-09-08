"""
Window class that creates a basic window using tkinter
"""

from tkinter import *
from tkinter import ttk

class Window:

    #constructor
    def __init__(self):
        #create tkinter window
        self.root = Tk()

        #toggle fullscreen using the escape key
        self.root.bind("<Escape>", self.toggleFull)

        #default to fullscreen
        self.full = True
        self.root.attributes("-fullscreen", True)

        #update the window so the dimensions change
        self.root.update()
        self.size = (
            (self.root.winfo_width()),
            (self.root.winfo_height())
            )

    def toggleFull(self, event):
         self.full = not(self.full)
         self.root.attributes("-fullscreen",self.full)

    def clearWindow(self):
         #delete all components of the root window
         for child in self.root.grid_slaves():
             child.grid_forget()
         
    def exit(self):

         #delete the root window
         self.root.destroy()
