import tkinter as tk
from tkinter import ttk


def greet():
    print("Hello Buttons App user !")


root = tk.Tk()

greet_button = ttk.Button(
    root, text="Greet", command=greet
)  # button that calls the function greet() when pressed
greet_button.pack(side="left", fill="both", expand=True)

quit_button = ttk.Button(
    root, text="Quit", command=root.destroy
)  # enable to close windows
quit_button.pack(side="left", fill="y")

root.mainloop()  # continue until the closing of the window
