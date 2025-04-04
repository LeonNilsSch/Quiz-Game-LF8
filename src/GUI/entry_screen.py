import tkinter as tk
from tkinter import ttk
from category_screen import category_screen  # Importiere category_screen.py


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

    # Spielen-Button
    btn_play = tk.Button(
        frame,
        text="Spiel starten",
        font=btn_font,
        bg=btn_bg,
        fg=btn_fg,
        relief="flat",
        command=open_category_screen,
    )
    btn_play.pack(pady=20, ipadx=20, ipady=10)

    # Beenden-Button
    btn_exit = tk.Button(
        frame,
        text="Beenden",
        font=btn_font,
        bg=btn_bg,
        fg=btn_fg,
        relief="flat",
        command=main_screen.destroy,
    )
    btn_exit.pack(pady=20, ipadx=20, ipady=10)

    main_screen.mainloop()
