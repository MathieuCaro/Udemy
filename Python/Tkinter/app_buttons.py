# ===========================================================================
# Title: app_buttons.py
# Description: This will create two buttons:first one to send a message, the
#   other one to quit and close the window
# Author : Mathieu Caro
# Source : Udemy
# ===========================================================================


# -----------------------------Import of modules-----------------------------
from tkinter import ttk  # tkk: set of widgets:buttons, labels...
import tkinter as tk  # tkinter: package for standard python interface

# ---------------------------------Functions----------------------------------


def greet():
    """Simply print a string in terminal"""
    print("Hello Buttons App user !")


def app_buttons(root):
    greet_button = ttk.Button(root, text="Greet", command=greet)
    # button that calls the function greet() when pressed
    greet_button.pack(side="left", fill="both", expand=True)
    # side : side of the window where the button is
    # fill : fill the free space of both side
    quit_button = ttk.Button(root, text="Quit", command=root.destroy)
    # enable to close windows
    # when the button is pushed, the windows is closed
    quit_button.pack(side="left", fill="y")

    root.mainloop()  # continue until the closing of the window


# ---------------------------------Main program-------------------------------
root = tk.Tk()  # creation of an object(root here)
app_buttons(root)  # packing_components_app
