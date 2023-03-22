# -----------------------------import of modules------------------------------
import tkinter as tk  # tkinter: package for standard python interface

# -------------------------------import of files------------------------------
from hello_world_app import hello_world_app
from packing_components import packing_components
from greeting_app import greeting_app

# ---------------------------------Main program-------------------------------
root = tk.Tk()  # creation of an object(root here)
hello_world_app(root)  # hello_world_app
packing_components(root)  # packing_components_app
greeting_app(root)  # greeting_app
