# -----------------------------import of modules------------------------------
import tkinter as tk

# -----------------------------Packing components-----------------------------


def packing_components(root):
    """App to browse the fonctionnality of geometry"""
    root.geometry("600x400")
    # geometry : define the initial dimensions of the windows
    rectangle_1 = tk.Label(root, text="Rectangle 1", bg="green", fg="white")
    # Label : space reserved to widget of type text
    # bg:background fg:foreground
    rectangle_1.pack(ipadx=10, ipady=10, fill="both", expand=True)
    # ipadx/ipady : internal padding x and y of the obect (here rectangle_1)
    # expand : the object takes up all space (if true)
    rectangle_2 = tk.Label(root, text="Rectangle 2", bg="red", fg="white")
    rectangle_2.pack(ipadx=10, ipady=10)
    root.mainloop()
    # mainloop: display the window and continue until the closing of the window
