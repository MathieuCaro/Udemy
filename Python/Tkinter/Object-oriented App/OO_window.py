# ===========================================================================
# Title: OO_window.py
# Description: This will create two buttons:first one to send a message, the
#   other one to quit and close the window
# Author : Mathieu Caro
# Source : Udemy
# ===========================================================================


# -----------------------------Import of modules-----------------------------
from tkinter import ttk  # tkk: set of widgets:buttons, labels...
import tkinter as tk  # tkinter: package for standard python interface

# ---------------------------------Functions----------------------------------


class HelloWorld(tk.Tk):
    def __init__(self):
        super().__init__()  # call the constructor of tk.Tk(super())
        self.title("Hello World")
        ttk.Label(self, text="Hello World").pack()


# ---------------------------------Main program-------------------------------
root = HelloWorld()  # creation of an object(root here)
root.title()
root.mainloop()
