# ===========================================================================
# Title: greeting_app_frame.py
# Description: This will reuse the fonction greeting_app but with grid
# Author : Mathieu Caro
# Source : Udemy
# ===========================================================================

# -----------------------------Import of modules------------------------------
import tkinter as tk  # tkinter: package for standard python interface
from tkinter import ttk  # tkk: set of widgets:buttons, labels...


# -----------------------------Global Variables--------------------------------

# ---------------------------------Functions----------------------------------


def greet(user_name):
    """Function that print "Hello" following by the name of the user"""
    print(f"Hello {user_name.get()} !")


def greeting_app(root, frame1, frame2):
    # Entry field
    user_name = tk.StringVar()  # create a variable of string
    name_label = ttk.Label(frame1, text="Name ")  # Label : space for text
    name_label.grid(row=0, column=0, padx=(0, 10))
    # label "name" put on the left side with a horizontal padding
    # of 0 on the left side and 10 on the right side of text
    name_entry = ttk.Entry(frame1, width=15, textvariable=user_name)
    # width in nb of characters
    name_entry.grid(row=0, column=1)
    name_entry.focus()
    # focus enable to enter text from the keyboard
    # Two buttons: greet and quit button
    greet_button = ttk.Button(frame2, text="Greet", command=lambda: greet(user_name))
    # button that calls the function greet() when pressed
    greet_button.grid(row=0, column=0, sticky="EW")
    # pack: enable to place the components into the window
    quit_button = ttk.Button(frame2, text="Quit", command=root.destroy)
    # enable to close windows
    quit_button.grid(row=0, column=1, sticky="EW")


# ---------------------------------Main program-------------------------------
root = tk.Tk()  # creation of an object(root here)
root.title("Greet")
root.columnconfigure(0, weight=1)
# The column 0 have a weight of 1(by default 0)

# input frame = frame exclusively reserve to the input text(name of the user)
# it takes all the top space
input_frame = ttk.Frame(root, padding=(20, 10, 20, 0))
# left:20 top:10 right:20 bottom:0
input_frame.grid(row=0, column=0, sticky="EW")
button_frame = ttk.Frame(root, padding=(20, 10))
# left : 20 right :10
button_frame.grid(row=1, column=0, sticky="EW")
# sticky: specify how a widget is aligned inside the cell of the grid
# with the cardinal point : E(East),N(North),etc...
# here EW means that it is stretched horizontally
button_frame.columnconfigure(0, weight=1)
button_frame.columnconfigure(1, weight=1)
greeting_app(root, input_frame, button_frame)  # greeting_app
root.mainloop()
