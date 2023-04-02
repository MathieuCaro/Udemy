# -----------------------------Import of modules------------------------------
import tkinter as tk  # tkinter: package for standard python interface
from tkinter import ttk  # tkk: set of widgets:buttons, labels...
from tkinter.constants import END


class MeterConverter(ttk.Frame):
    def __init__(self, container, **kwargs):
        # here self=root.frame
        super().__init__(container, **kwargs)

        # Creating Label widgets
        self.meter_label = ttk.Label(self, text="m")
        self.meter_value = tk.StringVar()
        self.meter_value_display = ttk.Entry(self, textvariable=self.meter_value)

        # Affichage des unités françaises
        self.km_label = ttk.Label(self, text="km")
        self.hm_label = ttk.Label(self, text="hm")
        self.dm_label = ttk.Label(self, text="dm")
        self.cm_label = ttk.Label(self, text="cm")
        self.mm_label = ttk.Label(self, text="mm")
        # Affichage unités anglo-saxones
        self.ml_label = ttk.Label(self, text="mile")
        self.yard_label = ttk.Label(self, text="yard")
        self.ft_label = ttk.Label(self, text="foot")
        self.inch_label = ttk.Label(self, text="inch")

        # Affichage des conversions
        self.km_text = tk.Text(self, height=1, width=15, pady=5)
        self.hm_text = tk.Text(self, height=1, width=15, pady=5)
        self.dm_text = tk.Text(self, height=1, width=15, pady=5)
        self.cm_text = tk.Text(self, height=1, width=15, pady=5)
        self.mm_text = tk.Text(self, height=1, width=15, pady=5)
        self.ml_text = tk.Text(self, height=1, width=15, pady=5)
        self.yard_text = tk.Text(self, height=1, width=15, pady=5)
        self.ft_text = tk.Text(self, height=1, width=15, pady=5)
        self.inch_text = tk.Text(self, height=1, width=15, pady=5)

        # Ajout du bouton "convertir"
        self.convert_bt = ttk.Button(self, text="Convertir", command=self.lengthconv)

        # Positionnement de la données d'entrée et de l'unité
        self.meter_label.grid(row=0, column=1, pady=10)
        self.meter_value_display.grid(row=0, column=0, padx=5, pady=10)

        # Positionnement du bouton
        self.convert_bt.grid(row=1, columnspan=2, sticky="EW", pady=10)

        # Positionnement résultats/unités
        self.km_text.grid(row=3, column=0)
        self.km_label.grid(row=3, column=1)

        self.hm_text.grid(row=4, column=0)
        self.hm_label.grid(row=4, column=1)

        self.dm_text.grid(row=5, column=0)
        self.dm_label.grid(row=5, column=1)

        self.cm_text.grid(row=6, column=0)
        self.cm_label.grid(row=6, column=1)

        self.mm_text.grid(row=7, column=0)
        self.mm_label.grid(row=7, column=1)

        self.ml_text.grid(row=8, column=0)
        self.ml_label.grid(row=8, column=1)

        self.yard_text.grid(row=9, column=0)
        self.yard_label.grid(row=9, column=1)

        self.ft_text.grid(row=10, column=0)
        self.ft_label.grid(row=10, column=1)

        self.inch_text.grid(row=11, column=0)
        self.inch_label.grid(row=11, column=1)

    def lengthconv(self):
        # ici on prend la valeur meter_value et le tronquer en float
        # puis on le multiplie par son coefficient multiplicateur
        km = float(self.meter_value.get()) * 1000
        hm = float(self.meter_value.get()) * 100
        dm = float(self.meter_value.get()) * 10
        cm = float(self.meter_value.get()) / 100
        mm = float(self.meter_value.get()) / 1000

        inch = float(self.meter_value.get()) * 39.37
        foot = float(self.meter_value.get()) * 3.28084
        yard = float(self.meter_value.get()) * 1.094
        mile = float(self.meter_value.get()) * 0.00062
        # delete prend ici la 1ere ligne(1) et la premieère colonne(0)
        # jusqu'à la fin(END), ici END est une constante de la librairie tkinter
        self.km_text.delete("1.0", END)
        self.km_text.insert(END, round(km, 3))

        self.hm_text.delete("1.0", END)
        self.hm_text.insert(END, round(hm, 3))

        self.dm_text.delete("1.0", END)
        self.dm_text.insert(END, round(dm, 3))

        self.cm_text.delete("1.0", END)
        self.cm_text.insert(END, round(cm, 3))

        self.mm_text.delete("1.0", END)
        self.mm_text.insert(END, round(mm, 3))

        self.ml_text.delete("1.0", END)
        self.ml_text.insert(END, round(mile, 3))

        self.yard_text.delete("1.0", END)
        self.yard_text.insert(END, round(yard, 3))

        self.ft_text.delete("1.0", END)
        self.ft_text.insert(END, round(foot, 3))

        self.inch_text.delete("1.0", END)
        self.inch_text.insert(END, round(inch, 3))


root = tk.Tk()
MeterConverter(root)
root.mainloop()
