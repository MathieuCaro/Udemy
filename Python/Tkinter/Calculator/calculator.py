# ===========================================================================
# Title: calculator.py
# Description: This program is a calculator
# Author : Mathieu Caro
# Source : Udemy
# ===========================================================================

# -----------------------------Import of modules------------------------------
import tkinter as tk  # tkinter: package for standard python interface
from tkinter import ttk  # tkk: set of widgets:buttons, labels...

# ----------------------------------Constants---------------------------------
ORANGE = "#FF7900"
BLACK = "#000000"
WHITE = "#FFFFFF"
BLUE = "#0090FC"
FONT_FAMILY = "Segoe UI"
FONT_STYLE_BUTTON = ("arial", 30, "bold")
TITLE = "Simple Calculator"
HEIGHT_WINDOW = 700
WIDTH_WINDOW = 550
COOR_X_FIRST = 100
COOR_Y_FIRST = 100
HORIZONTAL = "EW"  # East and West
VERTICAL = "NS"  # NorthSouth
ALL_SIDES = "NSEW"  # North South East West
ERROR = "ERROR"
WEIGHT_1 = 1


# -----------------------------Global Variables--------------------------------
EQUATION = ""
# ---------------------------------Functions----------------------------------

# This function enables to set the value of each button on screen


def show(value):
    global EQUATION
    EQUATION += value
    # we add each button value to the string equation
    label_result.set(EQUATION)
    # for each additional button pushed on calculator
    # it updates the value of the equation
    return label_result


# This function simply clear the equation after using the "C" button
def clear():

    global EQUATION
    EQUATION = ""
    label_result.set(EQUATION)
    return 0


# Intermediate function to transform a string into a result of the calculus
def string_to_calculate(EQUATION):
    nb_result = eval(EQUATION)
    return nb_result


# This function calculate from the string "equation"
def calculate():
    global EQUATION
    result = ""
    if EQUATION != "":
        try:
            result = string_to_calculate(EQUATION)
            # here eval enables from a string to transform into a calcul
            # in that way, eval send back the result of the operation
        except ValueError:
            result = "error"
            EQUATION = ""
            #  the operation is not calculable, there is an error
        label_result.set(result)
    return


def buttons_parameters(
    text_,
    width_,
    height_,
    foreground_color,
    backgroundcolor_,
    char,
    row_,
    column_
    # noqa: E501
):
    button = tk.Button(
        button_frame,
        fg=foreground_color,
        bg=backgroundcolor_,
        command=lambda: show(char),
        bd=1,
        pady=1,
        font=FONT_STYLE_BUTTON,
        height=height_,
        width=width_,
        text=text_,
    )
    button.grid(row=row_, column=column_)
    return
    # text_ = text on the button
    # width_ = width of the button
    # height_ = height of the button
    # foreground_color= fcg of the button
    # backgroundcolor_ = bgc of the color
    # char_ = value of the button(char),
    # row_ = row on the app
    # column_ = column on the app


# ---------------------------------Main program-------------------------------
root = tk.Tk()
# creation of an object(root here)
root.title(TITLE)
root.geometry(f"{WIDTH_WINDOW}x{HEIGHT_WINDOW}+{COOR_X_FIRST}+{COOR_Y_FIRST}")
print(root.winfo_exists())
print(type(root.winfo_geometry()))
# Size of the window(570*600)
# initial point (100px from de left and 200 from the top)
root.resizable(False, False)
# The size of the window can't be modified(by x or y)(False)
root.configure(bg=WHITE)
root.columnconfigure(0, weight=1)

# Result of the calculator
result_frame = ttk.Frame(root, padding=(20, 10, 20, 0))
result_frame.grid(row=0, column=0, sticky=HORIZONTAL)
result_frame.rowconfigure(0, weight=1)
label_result = tk.StringVar()
label = ttk.Label(result_frame, textvariable=label_result, anchor="e")
# anchor = position, here "EAST"
label.config(font=(FONT_FAMILY, 70))
label.grid(row=0, column=0, sticky=HORIZONTAL)

button_frame = ttk.Frame(root, padding=(20, 10))
button_frame.grid(row=1, column=0, sticky=ALL_SIDES)

# it enables to have 4 equal portions on screen horizontally
button_frame.columnconfigure(0, WEIGHT_1)
button_frame.columnconfigure(1, WEIGHT_1)
button_frame.columnconfigure(2, WEIGHT_1)
button_frame.columnconfigure(3, WEIGHT_1)
# it enables to have 4 equal portions on screen horizontally
button_frame.rowconfigure(0, WEIGHT_1, minsize=20)
button_frame.rowconfigure(1, WEIGHT_1, minsize=20)
button_frame.rowconfigure(2, WEIGHT_1, minsize=20)
button_frame.rowconfigure(3, WEIGHT_1, minsize=20)


# First line of digits
button_C = tk.Button(
    button_frame,
    text="C",
    width=3,
    height=2,
    font=FONT_STYLE_BUTTON,
    bd=1,
    fg=WHITE,
    bg=BLUE,
    pady=1,
    command=lambda: clear(),
)
button_C.grid(row=1, column=0)

button_div = buttons_parameters("/", 3, 2, WHITE, BLACK, "/", 1, 1)
button_percent = buttons_parameters("%", 3, 2, WHITE, BLACK, "%", 1, 2)
button_X = buttons_parameters("x", 3, 2, WHITE, BLACK, "*", 1, 3)

# Second line of digits
button_7 = buttons_parameters("7", 3, 2, WHITE, BLACK, "7", 2, 0)
button_8 = buttons_parameters("8", 3, 2, WHITE, BLACK, "8", 2, 1)
button_9 = buttons_parameters("9", 3, 2, WHITE, BLACK, "9", 2, 2)
button_min = buttons_parameters("-", 3, 2, WHITE, BLACK, "-", 2, 3)

# Third line of digits
button_4 = buttons_parameters("4", 3, 2, WHITE, BLACK, "4", 3, 0)
button_5 = buttons_parameters("5", 3, 2, WHITE, BLACK, "5", 3, 1)
button_6 = buttons_parameters("6", 3, 2, WHITE, BLACK, "6", 3, 2)
button_plus = buttons_parameters("+", 3, 2, WHITE, BLACK, "+", 3, 3)

# Forth line of digits
button_1 = buttons_parameters("1", 3, 2, WHITE, BLACK, "1", 4, 0)
button_2 = buttons_parameters("2", 3, 2, WHITE, BLACK, "2", 4, 1)
button_3 = buttons_parameters("3", 3, 2, WHITE, BLACK, "3", 4, 2)
button_equal = tk.Button(
    button_frame,
    text="=",
    width=3,
    height=4,
    font=FONT_STYLE_BUTTON,
    bd=1,
    fg=WHITE,
    bg=ORANGE,
    pady=1,
    command=lambda: calculate(),
)
button_equal.grid(row=4, column=3, rowspan=2, sticky=VERTICAL)

# Fifth line of digits
button_0 = tk.Button(
    button_frame,
    text="0",
    width=8,
    height=2,
    font=FONT_STYLE_BUTTON,
    bd=1,
    fg=WHITE,
    bg=BLACK,
    command=lambda: show("0"),
)
button_0.grid(row=5, column=0, columnspan=2, sticky=VERTICAL)
button_pt = tk.Button(
    button_frame,
    text=".",
    width=3,
    height=2,
    font=FONT_STYLE_BUTTON,
    bd=1,
    fg=WHITE,
    bg=BLACK,
    command=lambda: show("."),
)
button_pt.grid(row=5, column=2, sticky=VERTICAL)


root.mainloop()
