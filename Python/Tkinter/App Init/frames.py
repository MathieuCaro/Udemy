# ===========================================================================
# Title: frames.py
# Description: This will enable to understand the placement of the labels with
#   the frames, one to another
# Author : Mathieu Caro
# Source : Udemy
# ===========================================================================

# -----------------------------import of modules------------------------------
from tkinter import ttk  # tkk: set of widgets:buttons, labels...
import tkinter as tk  # tkinter: package for standard python interface

# ------------------------Packing components function--------------------------


def frame_options(root, main):
    tk.Label(main, text="Label top", bg="red").pack(
        side="top", expand=True, fill="both"
    )
    tk.Label(main, text="Label top", bg="red").pack(
        side="top", expand=True, fill="both"
    )
    # The both first labels share the left side by default
    tk.Label(root, text="Label left", bg="green").pack(
        side="left", expand=True, fill="both"
    )
    # This label occupies the leftmost free space(right side), the left side is
    # already occupied by the two first labels


# ---------------------------------Main program-------------------------------

root = tk.Tk()  # creation of an object(root here)
main = ttk.Frame()  # creation of the frame (main here)
main.pack(side="left", fill="both", expand=True)
# This frame will contain the both first labels(red) and be positionned on the
# left side of the window, take all the vertical left space

frame_options(root, main)
root.mainloop()
