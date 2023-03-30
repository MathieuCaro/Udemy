# ===========================================================================
# Title: scrollbars.py
# Description: This program allows you to discover a non-exhaustive list
#   of separators
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
root = tk.Tk()  # creation of an object(root here)
root.geometry("600x400")
root.resizable(False, False)
root.title("Text Widget example")

root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

ttk.Label(root, text="Hello, World", padding=20).pack()

ttk.Separator(root, orient="horizontal").pack(fill="x")

ttk.Label(root, text="Hello, World", padding=20).pack()

root.mainloop()
