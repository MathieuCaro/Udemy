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
# -----------------------------Global Variables--------------------------------
EQUATION = ""
# ---------------------------------Functions----------------------------------


def show(value):
    # This function enables to set the value of each button on screen
    global EQUATION
    EQUATION += value
    # we add each button value to the string equation
    label_result.set(EQUATION)
    # for each additional button value it updates the value of the equation


def clear():
    """This function simply clear the equation after using the "C" button"""
    global equation
    equation = ""
    label_result.set(equation)
    return 0


def calculate():
    """This function calculate from the string "equation" """
    global equation
    result = ""
    if equation != "":
        try:
            result = eval(equation)
            # here eval enables from a string to transform into a calcul
            # in that way, eval send back the result of the operation
        except ValueError:
            result = "error"
            equation = ""
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
        font=("arial", 30, "bold"),
        height=height_,
        width=width_,
        text=text_,
    )
    button.grid(row=row_, column=column_)
    return


# ---------------------------------Main program-------------------------------
root = tk.Tk()
# creation of an object(root here)
root.title("Simple Calculator")
root.geometry("550x700+100+200")
# Size of the window(570*600)
# initial point (100px from de left and 200 from the top)
root.resizable(False, False)
# The size of the window can't be modified(by x or y)(False)
root.configure(bg="white")
root.columnconfigure(0, weight=1)

# Result of the calculator
result_frame = ttk.Frame(root, padding=(20, 10, 20, 0))
result_frame.grid(row=0, column=0, sticky="EW")
result_frame.rowconfigure(0, weight=1)
label_result = tk.StringVar()
label = ttk.Label(result_frame, textvariable=label_result, anchor="e")
label.config(font=(FONT_FAMILY, 70))
label.grid(row=0, column=0, sticky="EW")

button_frame = ttk.Frame(root, padding=(20, 10))
button_frame.grid(row=1, column=0, sticky="NSEW")

button_frame.columnconfigure(0, weight=1)
button_frame.columnconfigure(1, weight=1)
button_frame.columnconfigure(2, weight=1)
button_frame.columnconfigure(3, weight=1)
button_frame.rowconfigure(0, weight=1, minsize=20)
button_frame.rowconfigure(1, weight=1, minsize=20)
button_frame.rowconfigure(2, weight=1, minsize=20)
button_frame.rowconfigure(3, weight=1, minsize=20)


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
button_1 = buttons_parameters("1", 3, 2, BLACK, BLACK, "1", 4, 0)
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
button_equal.grid(row=4, column=3, rowspan=2, sticky="NS")

# Fifth line of digits
button_0 = tk.Button(
    button_frame,
    text="0",
    width=7,
    height=2,
    font=("arial", 30, "bold"),
    bd=1,
    fg=WHITE,
    bg=BLACK,
    command=lambda: show("0"),
)
button_0.grid(row=5, column=0, columnspan=2, sticky="NS")
button_pt = tk.Button(
    button_frame,
    text=".",
    width=3,
    height=2,
    font=("arial", 30, "bold"),
    bd=1,
    fg=WHITE,
    bg=BLACK,
    command=lambda: show("."),
)
# buttons_parameters(".", 3, 2, WHITE, BLACK, ".", 5, 2)
button_pt.grid(row=5, column=2, sticky="NS")


root.mainloop()
