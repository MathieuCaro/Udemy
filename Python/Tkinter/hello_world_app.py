# ===========================================================================
# Title: hello_world.py
# Description: This will display on the window "Hello World"
# Author : Mathieu Caro
# Source : Udemy
# ===========================================================================

# -----------------------------import of modules------------------------------
from tkinter import ttk  # tkk: set of widgets:buttons, labels...
import tkinter as tk  # tkinter: package for standard python interface

# -----------------------------Hello world program----------------------------


def hello_world_app(root):
    """Simple app to display "Hello, world" into a window"""
    # root = tk.Tk()  # creation of an object(root here)
    ttk.Label(root, text="Hello,world", padding=(30, 10)).pack()
    # Label : space for text
    # pack: enable to place the components into the window
    root.mainloop()  # mainloop: display the window
    # and continue until the closing of the window


# ---------------------------------Main program-------------------------------
root = tk.Tk()  # creation of an object(root here)
hello_world_app(root)  # hello_world_app
