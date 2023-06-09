import tkinter as tk
from tkinter import ttk
 
class FeetToMeters:

    def __init__(self, root):
        # Configuration de la fenêtre principale
        root.title("Feet to Meters")
        root.resizable(False, False)

        # Création du cadre principal
        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

        # Entrée pour les pieds
        self.feet = tk.StringVar()
        feet_entry = ttk.Entry(mainframe, width=7, textvariable=self.feet)
        feet_entry.grid(column=2, row=1, sticky=(tk.W, tk.E))

        # Affichage des mètres
        self.meters = tk.StringVar()
        ttk.Label(mainframe, textvariable=self.meters).grid(column=2, row=2, sticky=(tk.W, tk.E))

        # Bouton de calcul
        ttk.Button(mainframe, text="Calculate", command=self.calculate).grid(column=3, row=3, sticky=tk.W)

        # Étiquettes de texte
        ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=tk.W)
        ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=tk.E)
        ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=tk.W)

        # Configuration des espacements entre les éléments
        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

        # Focus sur l'entrée et liaison de la touche Entrée au calcul
        feet_entry.focus()
        root.bind("<Return>", self.calculate)

    def calculate(self, *args):
        try:
            value = float(self.feet.get())
            self.meters.set(int(0.3048 * value * 10000.0 + 0.5) / 10000.0)
        except ValueError:
            pass

if __name__ == "__main__":
    root = tk.Tk()
    FeetToMeters(root)
    root.mainloop()
