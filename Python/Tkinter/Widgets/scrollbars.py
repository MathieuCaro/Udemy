# ===========================================================================
# Title: scrollbars.py
# Description: This program allows you to discover a non-exhaustive list
#   of scrollbars
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

# ---------------------------------Main program-------------------------------
root = tk.Tk()
# creation of an object(root here)
root.geometry("600x400")
root.resizable(False, False)
root.title("Scrollbar Widget example")

root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

text = tk.Text(root, height=8)
# height: number of rows
text.grid(row=0, column=0, sticky="EW")
text.insert("1.0", "Please enter a comment")

# scrollbar
text_scroll = ttk.Scrollbar(root, orient="vertical", command=text.yview)
# orient : tell that if the scrollbar is vertical or horizonal
# command : what happened when the scrollbar is moved
text_scroll.grid(row=0, column=1, sticky="ns")
text["yscrollcommand"] = text_scroll.set
# enable to link the text and the scrollbar

root.mainloop()
