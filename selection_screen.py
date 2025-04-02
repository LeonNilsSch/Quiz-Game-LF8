import tkinter as tk
from category_screen import category_screen  # Importiere die Funktion aus der difficultyscreen.py

# Funktion zum Starten des Spiels mit der Auswahl
def start_game_mode(mode):
    print(f"Spielmodus {mode} wurde ausgewählt!")
    choose_mode(mode)  # Rufe die Moduswahl-Funktion auf, um zum Schwierigkeitsbildschirm zu wechseln

# Funktion für die Auswahl des Modus
def choose_mode(mode):
    print(f"Ausgewählter Modus: {mode}")
    category_screen()  # Öffnet den Schwierigkeitsauswahl-Bildschirm nach der Moduswahl

def mode_screen():
    root = tk.Tk()
    root.title("Wähle deinen Modus")
    root.geometry("800x600")
    root.configure(bg="#2e2e2e")

    # Schriftarten und Farben
    label_font = ("Helvetica", 16, "bold")  # Moderne Schriftart
    entry_bg = "#3A3A3A"  # Mittelgrau für das Eingabefeld
    entry_fg = "#FFFFFF"  # Weißer Text für bessere Lesbarkeit
    btn_font = ("Helvetica", 14, "bold")  # Button-Schriftart
    btn_bg = "#444444"  # Dunkleres Grau für bessere Lesbarkeit
    btn_fg = "#DDDDDD"  # Hellgrau für bessere Lesbarkeit
    btn_hover_bg = "#555555"  # Leicht helleres Grau für Hover
    btn_border_width = 1  # Dünnerer Rahmen für macOS-Kompatibilität
    btn_border_color = "#666666"  # Noch dunkler für Rahmen

    # Styling für macOS-kompatible Buttons
    root.option_add('*TButton*background', btn_bg)
    root.option_add('*TButton*foreground', btn_fg)
    root.option_add('*TButton*borderwidth', btn_border_width)
    root.option_add('*TButton.padding', [15, 10])  # Mehr Padding für die Buttons

    # Frame zum vollständigen Zentrieren
    frame = tk.Frame(root, bg="#2e2e2e")
    frame.place(relx=0.5, rely=0.5, anchor="center")

    # Modus-Auswahl
    tk.Label(frame, text="Wählen Sie den Spielmodus", font=label_font, fg="white", bg="#2e2e2e").pack(pady=20)

    # Buttons für Spielmodi mit Emojis
    btn_singleplayer = tk.Button(frame, text="🎮 Singleplayer", font=btn_font, relief="flat", bd=btn_border_width, command=lambda: start_game_mode("Singleplayer"))
    btn_singleplayer.pack(pady=30, ipadx=40, ipady=20)  # Mehr Padding

    btn_multiplayer = tk.Button(frame, text="🤝 Multiplayer", font=btn_font, relief="flat", bd=btn_border_width, command=lambda: start_game_mode("Multiplayer"))
    btn_multiplayer.pack(pady=30, ipadx=40, ipady=20)  # Mehr Padding

    # Button Hover-Effekt und Cursor ändern
    def on_enter(event, button):
        button.config(bg=btn_hover_bg)
        button.config(cursor="hand2")  # Cursor zu Hand-Cursor ändern

    def on_leave(event, button):
        button.config(bg=btn_bg)
        button.config(cursor="")  # Cursor zurücksetzen

    btn_singleplayer.bind("<Enter>", lambda event, button=btn_singleplayer: on_enter(event, button))
    btn_singleplayer.bind("<Leave>", lambda event, button=btn_singleplayer: on_leave(event, button))

    btn_multiplayer.bind("<Enter>", lambda event, button=btn_multiplayer: on_enter(event, button))
    btn_multiplayer.bind("<Leave>", lambda event, button=btn_multiplayer: on_leave(event, button))

    root.mainloop()