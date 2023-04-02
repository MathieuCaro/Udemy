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


class Calculatrice(ttk.Frame):
    def __init__(self, container, **kwargs):
        super().__init__(container, **kwargs)
        # self.master = master
        # master.title("Ma fenêtre")
        # master.title(TITLE)
        # master.geometry(f"{WIDTH_WINDOW}x{HEIGHT_WINDOW}+{COOR_X_FIRST}+{COOR_Y_FIRST}")
        # Size of the window(570*600)
        # initial point (100px from de left and 200 from the top)
        # master.resizable(False, False)
        # The size of the window can't be modified(by x or y)(False)
        # master.configure(bg=WHITE)
        # master.columnconfigure(0, weight=1)
        # print(self.winfo_height)
        # Result of the calculator
        self.label_title = ttk.Label(self, text="Bonjour")
        self.result_frame = ttk.Frame(self, padding=(20, 5, 10, 0))

        self.result_frame.grid(row=0, column=0, sticky=HORIZONTAL)
        self.result_frame.rowconfigure(0, weight=1)
        self.label_result = tk.StringVar()
        self.label = ttk.Label(
            self.result_frame, textvariable=self.label_result, anchor="e"
        )
        # anchor = poself.sition, here "EAST"
        self.label.config(font=(FONT_FAMILY, 30))
        self.label.grid(row=0, column=0, sticky=HORIZONTAL)

        self.button_frame = ttk.Frame(self, padding=(20, 10))
        self.button_frame.grid(row=1, column=0, sticky=ALL_SIDES)

        # it enables to have 4 equal portions on screen horizontally
        self.button_frame.columnconfigure(0)
        self.button_frame.columnconfigure(1)
        self.button_frame.columnconfigure(2)
        self.button_frame.columnconfigure(3)
        # it enables to have 4 equal portions on screen horizontally
        self.button_frame.rowconfigure(0, minsize=20)
        self.button_frame.rowconfigure(1, minsize=20)
        self.button_frame.rowconfigure(2, minsize=20)
        self.button_frame.rowconfigure(3, minsize=20)

        # First line of digits
        self.button_C = tk.Button(
            self.button_frame,
            text="C",
            width=1,
            height=1,
            font=FONT_STYLE_BUTTON,
            bd=1,
            fg=WHITE,
            bg=BLUE,
            pady=1,
            command=lambda: self.clear(),
        )
        self.button_C.grid(row=1, column=0)

        self.button_div = self.buttons_parameters("/", 1, 1, WHITE, BLACK, "/", 1, 1)
        self.button_percent = self.buttons_parameters(
            "%", 1, 1, WHITE, BLACK, "%", 1, 2
        )
        self.button_X = self.buttons_parameters("x", 1, 1, WHITE, BLACK, "*", 1, 3)

        # Second line of digits
        self.button_7 = self.buttons_parameters("7", 1, 1, WHITE, BLACK, "7", 2, 0)
        self.button_8 = self.buttons_parameters("8", 1, 1, WHITE, BLACK, "8", 2, 1)
        self.button_9 = self.buttons_parameters("9", 1, 1, WHITE, BLACK, "9", 2, 2)
        self.button_min = self.buttons_parameters("-", 1, 1, WHITE, BLACK, "-", 2, 3)

        # Third line of digits
        self.button_4 = self.buttons_parameters("4", 1, 1, WHITE, BLACK, "4", 3, 0)
        self.button_5 = self.buttons_parameters("5", 1, 1, WHITE, BLACK, "5", 3, 1)
        self.button_6 = self.buttons_parameters("6", 1, 1, WHITE, BLACK, "6", 3, 2)
        self.button_plus = self.buttons_parameters("+", 1, 1, WHITE, BLACK, "+", 3, 3)

        # Forth line of digits
        self.button_1 = self.buttons_parameters("1", 1, 1, WHITE, BLACK, "1", 4, 0)
        self.button_2 = self.buttons_parameters("2", 1, 1, WHITE, BLACK, "2", 4, 1)
        self.button_3 = self.buttons_parameters("3", 1, 1, WHITE, BLACK, "3", 4, 2)
        self.button_equal = tk.Button(
            self.button_frame,
            text="=",
            width=1,
            height=2,
            font=FONT_STYLE_BUTTON,
            bd=1,
            fg=WHITE,
            bg=ORANGE,
            pady=1,
            command=lambda: self.calculate(),
        )
        self.button_equal.grid(row=4, column=3, rowspan=2, sticky=VERTICAL)

        # Fifth line of digits
        self.button_0 = tk.Button(
            self.button_frame,
            text="0",
            width=3,
            height=1,
            font=FONT_STYLE_BUTTON,
            bd=1,
            fg=WHITE,
            bg=BLACK,
            command=lambda: self.show("0"),
        )
        self.button_0.grid(row=5, column=0, columnspan=2, sticky=VERTICAL)
        self.button_pt = tk.Button(
            self.button_frame,
            text=".",
            width=1,
            height=1,
            font=FONT_STYLE_BUTTON,
            bd=1,
            fg=WHITE,
            bg=BLACK,
            command=lambda: self.show("."),
        )
        self.button_pt.grid(row=5, column=2, sticky=VERTICAL)

    def show(self, value):
        global EQUATION
        EQUATION += value
        # we add each button value to the string equation
        self.label_result.set(EQUATION)
        # for each additional button pushed on calculator
        # it updates the value of the equation
        return self.label_result

    # This function simply clear the equation after using the "C" button
    def clear(self):

        global EQUATION
        EQUATION = ""
        self.label_result.set(EQUATION)
        return 0

    # Intermediate function to transform a string into a result of the calculus
    def string_to_calculate(self, EQUATION):
        nb_result = round(eval(EQUATION), 3)
        return nb_result

    # This function calculate from the string "equation"
    def calculate(self):
        global EQUATION
        result = ""
        if EQUATION != "":
            try:
                result = self.string_to_calculate(EQUATION)
                # here eval enables from a string to transform into a calcul
                # in that way, eval send back the result of the operation
            except ValueError:
                result = "error"
                EQUATION = ""
                #  the operation is not calculable, there is an error
            self.label_result.set(result)
        return

    def buttons_parameters(
        self,
        text_,
        width_,
        height_,
        foreground_color,
        backgroundcolor_,
        char,
        row_,
        column_,
    ):
        self.button = tk.Button(
            self.button_frame,
            fg=foreground_color,
            bg=backgroundcolor_,
            command=lambda: self.show(char),
            bd=1,
            pady=1,
            font=FONT_STYLE_BUTTON,
            height=height_,
            width=width_,
            text=text_,
        ).grid(row=row_, column=column_)
