import tkinter as tk
from tkinter import ttk


class View(tk.Tk):

    PAD = 10
    MAX_BUTTON_PER_ROW = 4

    button_caption = [
        "C",
        "+/-",
        "%",
        "/",
        7,
        8,
        9,
        "*",
        4,
        5,
        6,
        "-",
        1,
        2,
        3,
        "+",
        0,
        ".",
        "=",
        "/",
    ]

    def __init__(self, controller):
        super().__init__()
        self.title("Calculatrice")
        self.controller = controller
        self.value_var = tk.StringVar()

        self._make_main_frame()
        self._make_entry()
        self._make_button()

    def main(self):
        self.mainloop()

    def _make_main_frame(self):
        self.frame = ttk.Frame(self)
        self.frame.pack(padx=self.PAD, pady=self.PAD)

    def _make_entry(self):
        entry = ttk.Entry(
            self.frame, textvariable=self.value_var, justify="right", state="disabled"
        )
        entry.pack(fill="x")

    def _make_button(self):
        outer_frame_btn = ttk.Frame(self.frame)
        outer_frame_btn.pack()

        frm = ttk.Frame(outer_frame_btn)
        frm.pack()

        buttons_in_row = 0

        for caption in self.button_caption:
            if buttons_in_row == self.MAX_BUTTON_PER_ROW:
                frm = ttk.Frame(outer_frame_btn)
                frm.pack()
                buttons_in_row = 0
            btn = ttk.Button(
                frm,
                text=caption,
                command=lambda button=caption: self.controller.on_button_click(button),
            )
            btn.pack(side="left")
            buttons_in_row += 1
