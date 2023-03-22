# import tkinter as tk  # tkinter: package for standard python interface
from tkinter import ttk  # tkk: set of widgets:buttons, labels...


def hello_world_app(root):
    """Simple app to display "Hello, world" into a window"""
    # root = tk.Tk()  # creation of an object(root here)
    ttk.Label(root, text="Hello,world", padding=(30, 10)).pack()
    # Label : space for text
    # pack: enable to place the components into the window
    root.mainloop()  # mainloop: display the window
    # and continue until the closing of the window
