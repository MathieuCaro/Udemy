# ===========================================================================
# Title: comboboxes.py
# Description: This program allows you to discover a non-exhaustive list
#   of comboboxes
# Author : Mathieu Caro
# Source : Udemy
# ===========================================================================

# -----------------------------Import of modules------------------------------
import tkinter as tk

# tkinter: package for standard python interface
from tkinter import ttk

# tkk: set of widgets:buttons, labels...

# -----------------------------Global Variables--------------------------------

# ---------------------------------Functions----------------------------------


def handle_selection(event):
    print("Today is", selected_weekday.get())
    print("But we're gonna change it to Friday")
    selected_weekday.set("Sunday")
    print(weekday.current())


# ---------------------------------Main program-------------------------------
root = tk.Tk()
# creation of an object(root here)
root.geometry("600x400")
root.resizable(False, False)
root.title("Checkbutton Widget example")

selected_weekday = tk.StringVar()
weekday = ttk.Combobox(root, textvariable=selected_weekday)
weekday["values"] = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
)
weekday["state"] = "readonly"
weekday.pack()

weekday.bind("<<ComboboxSelected>>", handle_selection)

root.mainloop()

print(selected_weekday.get(), " was selected")
