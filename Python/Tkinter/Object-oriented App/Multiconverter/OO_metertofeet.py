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

# -----------------------------Global Variables--------------------------------
APP_TITLE = "Distance converter"
METER_LABEL_FONT = ("Segoe UI", 15)
# ---------------------------------Functions----------------------------------

# This class represents the frame(container)
class MeterToFeet(ttk.Frame):
    def __init__(self, container, **kwargs):
        # here self=root.frame
        super().__init__(container, **kwargs)
        # These both values are objects of the Frame
        self.meters_value = tk.StringVar()
        self.feets_value = tk.StringVar()
        self.bind("<Return>", self.calculate_feet)
        # enable to calculate the number of feets
        # since the user press Enter on the keyboard
        self.bind("<KP_Enter>", self.calculate_feet)
        # enable to calculate the number of feets
        # since the user press Enter on the keyboard of numeric keypad

        # Widgets
        meters_label = ttk.Label(self, text="Meters:")
        meters_input = ttk.Entry(
            self, width=10, textvariable=self.meters_value, font=METER_LABEL_FONT
        )
        feet_label = ttk.Label(self, text="Feet:")
        feet_display = ttk.Label(self, textvariable=self.feets_value)
        calculate_button = ttk.Button(
            self, text="Calculate", command=self.calculate_feet
        )
        # Layout: grid definition
        meters_label.grid(column=0, row=0, sticky="W")
        meters_input.grid(column=1, row=0, sticky="EW")
        meters_input.focus()  # enable to type on it directly

        feet_label.grid(column=0, row=1, sticky="W")
        feet_display.grid(column=1, row=1, sticky="EW")

        calculate_button.grid(column=0, row=2, columnspan=2, sticky="EW")

        # it enables to configure every elements
        # by assigning padding for x and y
        for child in self.winfo_children():
            child.grid_configure(padx=15, pady=15)

    def calculate_feet(self, *args):
        try:
            meters = float(self.meters_value.get())
            feet = meters * 3.28084
            self.feets_value.set(f"{feet:.3f}")
        except ValueError:
            pass


# ---------------------------------Main program-------------------------------


# root = DistanceConverter()
# root.title(APP_TITLE)
# root.mainloop()
