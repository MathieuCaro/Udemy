# ===========================================================================
# Title: distance_converter.py
# Description: This program is an app to convert the distance
# Author : Mathieu Caro
# Source : Udemy
# ===========================================================================

# -----------------------------Import of modules------------------------------
import tkinter as tk  # tkinter: package for standard python interface
import tkinter.font as font
from tkinter import ttk  # tkk: set of widgets:buttons, labels...

# -----------------------------Global Variables--------------------------------

# ---------------------------------Functions----------------------------------


def calculate_feet(*args):
    try:
        meters = float(meters_value.get())
        feet = meters * 3.28084
        # print(f"{meters} meters equal to {feet:.3f} feets.")
        feets_value.set(f"{feet:.3f}")
    except ValueError:
        pass


# ---------------------------------Main program-------------------------------
root = tk.Tk()  # creation of an object(root here)
root.title("Distance converter")

font.nametofont("TkDefaultFont").configure(size=15)

meters_value = tk.StringVar()
feets_value = tk.StringVar(value="Feet shown here")

root.columnconfigure(0, weight=1)

main = ttk.Frame(root, padding=(30, 15))
main.grid()

meters_label = ttk.Label(main, text="Meters:")
meters_input = ttk.Entry(
    main, width=10, textvariable=meters_value, font=("Segoe UI", 15)
)
feet_label = ttk.Label(main, text="Feet:")
feet_display = ttk.Label(main, textvariable=feets_value)
calculate_button = ttk.Button(main, text="Calculate", command=calculate_feet)

# Grid definition
meters_label.grid(column=0, row=0, sticky="W")
meters_input.grid(column=1, row=0, sticky="EW")
meters_input.focus()  # enable to type on it directly

feet_label.grid(column=0, row=1, sticky="W")
feet_display.grid(column=1, row=1, sticky="EW")

calculate_button.grid(column=0, row=2, columnspan=2, sticky="EW")

for child in main.winfo_children():
    child.grid_configure(padx=15, pady=15)

root.bind("<Return>", calculate_feet)
# enable to calculate the number of feets
# since the user press Enter on the keyboard
root.bind("<KP_Enter>", calculate_feet)
# enable to calculate the number of feets
# since the user press Enter on the keyboard of numeric keypad

root.mainloop()
