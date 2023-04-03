# ===========================================================================
# Title: labels.py
# Description: This program allows you to discover a non-exhaustive list
#   of text box (insert and retrieve)
# Author : Mathieu Caro
# Source : Udemy
# ===========================================================================

# -----------------------------Import of modules------------------------------
import tkinter as tk  # tkinter: package for standard python interface
from tkinter import ttk  # tkk: set of widgets:buttons, labels...

# -----------------------------Global Variables--------------------------------

# ---------------------------------Functions----------------------------------


# ---------------------------------Main program-------------------------------
root = tk.Tk()  # creation of an object(root here)
root.geometry("600x400")
root.resizable(False, False)
root.title("Text Widget example")

text = tk.Text(root, height=8)  # height: number of rows
text.pack()

text.insert("1.0", "Please enter a comment...")
# First parameter : position of text (here first line(1)
# and from character 0(0))
# Second parameter : Text to display
text["state"] = "normal"  # by default or "disabled"

# how to get the content of the text area
text_content = text.get("1.0", "end")  # get the content of the text in
# the text box
# 1.0 : starting position
# end : ending position
print(text_content)

root.mainloop()
