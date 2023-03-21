import tkinter as tk
from tkinter import ttk


def greet():
    print(f"Hello {user_name.get()} !")


root = tk.Tk()

user_name = tk.StringVar()

name_label = ttk.Label(root, text="Name ")
name_label.pack(side="left", padx=(0, 10))  #
name_entry = ttk.Entry(
    root, width=15, textvariable=user_name
)  # width in nb of characters
name_entry.pack(side="left")
name_entry.focus()

greet_button = ttk.Button(
    root, text="Greet", command=greet
)  # button that calls the function greet() when pressed
greet_button.pack(side="left")

quit_button = ttk.Button(
    root, text="Quit", command=root.destroy
)  # enable to close windows
quit_button.pack(side="right")

root.mainloop()  # continue until the closing of the window
