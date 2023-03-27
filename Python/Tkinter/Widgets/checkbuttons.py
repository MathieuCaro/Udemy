# ===========================================================================
# Title: scrollbars.py
# Description: This program allows you to discover a non-exhaustive list 
#   of scrollbars
# Author : Mathieu Caro
# Source : Udemy
# ===========================================================================

# -----------------------------Import of modules------------------------------
import tkinter as tk  # tkinter: package for standard python interface
from tkinter import ttk  # tkk: set of widgets:buttons, labels...
# -----------------------------Global Variables--------------------------------

# ---------------------------------Functions----------------------------------

def print_current_option():
    print(selected_option.get())



# ---------------------------------Main program-------------------------------
root = tk.Tk()  # creation of an object(root here)
root.geometry("600x400")
root.resizable(False,False)
root.title("Scrollbar Widget example")

selected_option = tk.StringVar() 
#create a string variable (On or Off)

#creation of the checkbutton
check_button = ttk.Checkbutton(
    root, 
    text="Check Example",
    variable=selected_option,
    command=print_current_option,
    onvalue="On",
    offvalue="Off"
    ).pack()
#variable: correspond to the string variable(selected_option)
#command : function run when the button is checked or unchecked
#onvalue/offvalue : determined what value the variable take



root.mainloop() 