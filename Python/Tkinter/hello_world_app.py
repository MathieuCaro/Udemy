import tkinter as tk  # tkinter: package for standard python interface
from tkinter import ttk  # tkk: set of widgets:buttons, labels...

root = tk.Tk()  # creation of an object
ttk.Label(
    root, text="Hello,world", padding=(30, 10)
).pack()  # pack: enable to place the components into the window


root.mainloop()  # continue until the closing of the window
