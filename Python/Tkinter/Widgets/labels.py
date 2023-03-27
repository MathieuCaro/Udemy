# ===========================================================================
# Title: labels.py
# Description: This program allows you to discover a non-exhaustive list 
#   of label functionalities
# Author : Mathieu Caro
# Source : Udemy
# ===========================================================================

# -----------------------------Import of modules------------------------------
import tkinter as tk  # tkinter: package for standard python interface
from tkinter import ttk  # tkk: set of widgets:buttons, labels...
from PIL import Image,ImageTk #PIL : package to include images in a label
# -----------------------------Global Variables--------------------------------

# ---------------------------------Functions----------------------------------





# ---------------------------------Main program-------------------------------
root = tk.Tk()  # creation of an object(root here)
root.geometry("600x400")
root.resizable(False,False)
root.title("Label example")

#Text label
# label = ttk.Label(root,text="Hello, World ! ",padding=20)
# label.config(font=("Segoe UI",20))

#Image label
#enable to add an image to the label by its path
# image = Image.open("/mnt/c/c/Udemy/Udemy/Python/Tkinter/Widgets/thales.png")
#creating an image Tk
# photo = ImageTk.PhotoImage(image)
# label= ttk.Label(root,text="Image with text.",image=photo,padding=5,compound="right")
# compound enables to adjust text and image positionning

greeting = tk.StringVar()
label=ttk.Label(root,padding=10,textvariable=greeting)
label.pack()

greeting.set("Hello !")

root.mainloop()
