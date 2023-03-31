# ===========================================================================
# Title: OO_window.py
# Description: This app is the Hello world app, sendind the name entered by the
# the user, all this by classes
# Author : Mathieu Caro
# Source : Udemy
# ===========================================================================

# -----------------------------Global Variables-----------------------------


# -----------------------------Import of modules-----------------------------

# tkk: set of widgets:buttons, labels...
from tkinter import ttk

# tkinter: package for standard python interface
import tkinter as tk


# ---------------------------------Functions----------------------------------


class Hello_World(tk.Tk):
    # init method
    def __init__(self):
        # Call the constructor of the super class
        super().__init__()
        # Title of the App
        self.title("Hello World App")
        UserInputFrame(self).pack()


class UserInputFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.user_input = tk.StringVar(
            self,
        )

        label = ttk.Label(self, text="Enter your name:")
        entry_field = ttk.Entry(self, textvariable=self.user_input)
        # We assign to a command a method class
        button = ttk.Button(self, command=self.greet, text="OK")

        label.pack(side="left")
        entry_field.pack(side="left")
        button.pack(side="left")

    def greet(self):
        print(f"Hello, {self.user_input.get()}!")


# ---------------------------------Main program-------------------------------

root = Hello_World()


root.mainloop()
