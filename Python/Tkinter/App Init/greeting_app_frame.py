# ===========================================================================
# Title: greeting_app_frame.py
# Description: This will reuse the fonction greeting_app but with frames
# Author : Mathieu Caro
# Source : Udemy
# ===========================================================================

# -----------------------------Import of modules------------------------------
import tkinter as tk  # tkinter: package for standard python interface
from tkinter import ttk  # tkk: set of widgets:buttons, labels...

# -----------------------------Global Variables--------------------------------
LEFT = "left"
RIGHT = "right"
BOTH_SIDES = "both"
# ---------------------------------Functions----------------------------------


def greet(user_name):
    # Function that print "Hello" following by the name of the user
    print(f"Hello {user_name.get()} !")


def greeting_app(root, frame1, frame2):
    # Entry field
    user_name = tk.StringVar()  # create a variable of string
    name_label = ttk.Label(frame1, text="Name ")  # Label : space for text
    name_label.pack(side=LEFT, padx=(0, 10))
    # label "name" put on the left side with a horizontal padding
    # of 0 on the left side and 10 on the right side of text
    name_entry = ttk.Entry(frame1, width=15, textvariable=user_name)
    # width in nb of characters
    name_entry.pack(side=LEFT)
    name_entry.focus()
    # focus enable to enter text from the keyboard
    # Two buttons: greet and quit button
    greet_button = ttk.Button(
        frame2, text="Greet", command=lambda: greet(user_name)
    )  # noqa: E501
    # button that calls the function greet() when pressed
    greet_button.pack(side=LEFT, fill="x", expand=True)
    # pack: enable to place the components into the window
    quit_button = ttk.Button(frame2, text="Quit", command=root.destroy)
    # enable to close windows
    quit_button.pack(side=RIGHT, fill="x", expand=True)


# ---------------------------------Main program-------------------------------
root = tk.Tk()  # creation of an object(root here)
# input frame = frame exclusively reserve to the input text(name of the user)
# it takes all the top space
input_frame = ttk.Frame(root, padding=(20, 10, 20, 0))
# left:20 top:10 right:20 bottom:0
input_frame.pack(fill=BOTH_SIDES)
button_frame = ttk.Frame(root, padding=(20, 10))
# left : 20 right :10
button_frame.pack(fill=BOTH_SIDES)
greeting_app(root, input_frame, button_frame)  # greeting_app
root.mainloop()
