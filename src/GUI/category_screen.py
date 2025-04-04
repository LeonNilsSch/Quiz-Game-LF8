import sys
import os

# Füge den Hauptordner zum Python-Suchpfad hinzu
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import tkinter as tk
from selection_screen import (
    mode_screen,
)  # Importiere mode_screen aus selection_screen.py


def category_screen():
    root = tk.Tk()
    root.title("Wähle die Kategorie")
    root.geometry("1200x800")
    root.configure(bg="#2e2e2e")  # Standard-Hintergrundfarbe

    # Schriftarten und Farben
    label_font = ("Helvetica", 16, "bold")
    btn_font = ("Helvetica", 14, "bold")
    btn_bg = "#444444"  # Dunkleres Grau für Buttons
    btn_fg = "#DDDDDD"  # Hellgrauer Text

    # Frame zum vollständigen Zentrieren
    frame = tk.Frame(root, bg="#2e2e2e")
    frame.place(relx=0.5, rely=0.5, anchor="center")

    # Kategorie-Auswahl Label
    tk.Label(
        frame,
        text="Wählen Sie Ihre Kategorie aus",
        font=label_font,
        fg="white",
        bg="#2e2e2e",
    ).pack(pady=20)

    # Buttons für Kategorien
    categories = [
        "Politik",
        "Geographie",
        "General Knowledge",
        "Film/Kino",
        "Videospiele",
        "Anime/Manga",
    ]

    for category in categories:
        btn = tk.Button(
            frame,
            text=category,
            font=btn_font,
            bg=btn_bg,
            fg=btn_fg,
            relief="flat",
            command=lambda c=category: open_mode_screen(root),
        )
        btn.pack(pady=15, ipadx=10, ipady=10)

    root.mainloop()


def open_mode_screen(root):
    """
    Öffnet den Modus-Bildschirm und schließt den Kategorie-Bildschirm.
    """
    root.destroy()  # Schließt den Kategorie-Bildschirm
    mode_screen()
