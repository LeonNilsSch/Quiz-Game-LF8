import tkinter as tk
from tkinter import ttk
from category_screen import category_screen  # Importiere category_screen.py
from achievement_screen import achievement_screen  # Importiere die Achievement-Screen-Funktion


# Funktion, um die Kategorieauswahl zu öffnen
def open_category_screen():
    main_screen.destroy()  # Schließt den Entry Screen
    category_screen()  # Öffnet die Kategorieauswahl


# Hauptbildschirm (Entry Screen)
def entry_screen():
    global main_screen
    main_screen = tk.Tk()
    main_screen.title("Hauptmenü")
    main_screen.geometry("1200x800")
    main_screen.configure(bg="#2e2e2e")  # Standard-Hintergrundfarbe

    # Schriftarten und Farben
    label_font = ("Helvetica", 16, "bold")
    btn_font = ("Helvetica", 14, "bold")
    btn_bg = "#444444"  # Dunkleres Grau für Buttons
    btn_fg = "#DDDDDD"  # Hellgrauer Text

    # Frame zum vollständigen Zentrieren
    frame = tk.Frame(main_screen, bg="#2e2e2e")
    frame.place(relx=0.5, rely=0.5, anchor="center")

    # Titel-Label
    tk.Label(
        frame,
        text="Willkommen im Quiz-Spiel!",
        font=label_font,
        fg="white",
        bg="#2e2e2e",
    ).pack(pady=20)

    # Button zur Kategorieauswahl
    tk.Button(
        frame,
        text="Kategorie auswählen",
        font=btn_font,
        bg=btn_bg,
        fg=btn_fg,
        relief="flat",
        command=open_category_screen,
    ).pack(pady=10, ipadx=20, ipady=10)

    # Button zu den Achievements
    tk.Button(
        frame,
        text="Achievements anzeigen",
        font=btn_font,
        bg=btn_bg,
        fg=btn_fg,
        relief="flat",
        command=open_achievement_screen,
    ).pack(pady=10, ipadx=20, ipady=10)

    main_screen.mainloop()

def open_achievement_screen():
    main_screen.destroy()  # Schließt den Entry Screen
    achievement_screen()  # Öffnet die Achievement-Screen-Funktion
