# -----------------------------Import of modules------------------------------
import tkinter as tk  # tkinter: package for standard python interface
from tkinter import ttk  # tkk: set of widgets:buttons, labels...

# -----------------------------Global Variables--------------------------------

# ---------------------------------Functions----------------------------------


def greet(user_name):
    """Function that print "Hello" following by the name of the user"""
    print(f"Hello {user_name.get()} !")


def greeting_app(root):
    user_name = tk.StringVar()  # create a variable of string
    name_label = ttk.Label(root, text="Name ")  # Label : space for text
    name_label.pack(side="left", padx=(0, 10))
    # label "name" put on the left side with a horizontal padding
    # of 0 on the left side and 10 on the right side of text
    name_entry = ttk.Entry(root, width=15, textvariable=user_name)
    # width in nb of characters
    name_entry.pack(side="left")
    name_entry.focus()
    # focus enable to enter text from the keyboard
    greet_button = ttk.Button(root, text="Greet", command=lambda: greet(user_name))
    # button that calls the function greet() when pressed
    greet_button.pack(side="left")
    # pack: enable to place the components into the window
    quit_button = ttk.Button(root, text="Quit", command=root.destroy)
    # enable to close windows
    quit_button.pack(side="right")


# ---------------------------------Main program-------------------------------
root = tk.Tk()  # creation of an object(root here)
greeting_app(root)  # greeting_app
