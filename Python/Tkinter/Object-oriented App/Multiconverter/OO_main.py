# ===========================================================================
# Title: OO_distance_converter.py
# Description: This program is an app to convert the distance from meters to
# feets by using classes
# Author : Mathieu Caro
# Source : Udemy
# ===========================================================================

# -----------------------------Import of modules------------------------------
import tkinter as tk  # tkinter: package for standard python interface
import tkinter.font as font
from tkinter import ttk  # tkk: set of widgets:buttons, labels...

from OO_calculator import Calculatrice
from OO_metertofeet import MeterToFeet
from OO_hello_world import UserInputFrame
from OO_meter_converter import MeterConverter

# -----------------------------Global Variables--------------------------------
APP_TITLE = "MULTI TOOLS APP"
METER_LABEL_FONT = ("Segoe UI", 20)
# ---------------------------------Functions----------------------------------

# Here this the main class(all the app)
class MainClass(tk.Tk):
    def __init__(self, *args, **kwargs):
        # self = root
        # kwargs : positionnal arguments
        # args : names arguments
        super().__init__(*args, **kwargs)

        self.title(APP_TITLE)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        frame1 = MeterConverter(self)
        frame1.grid(row=0, column=0)
        frame2 = Calculatrice(self)
        frame2.grid(row=0, column=1)
        frame3 = MeterToFeet(self)
        frame3.grid(row=1, column=0)
        frame4 = UserInputFrame(self)
        frame4.grid(row=1, column=1)


# ---------------------------------Main program-------------------------------


root = MainClass()
root.title(APP_TITLE)
root.mainloop()
