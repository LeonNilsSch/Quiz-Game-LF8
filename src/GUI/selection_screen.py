import tkinter as tk
from gameplay_screen import GameplayScreen  # Importiere den GameplayScreen

# Funktion zum Starten des Spiels mit der Auswahl
def start_game_mode(mode):
    if mode == "Singleplayer":
        # Beispiel: Kategorie-ID 1 (dies kann dynamisch übergeben werden, je nach vorheriger Auswahl)
        GameplayScreen(category_id=1)
    elif mode == "Multiplayer":
        print("Multiplayer-Modus ist noch nicht implementiert.")
    else:
        print(f"Unbekannter Modus: {mode}")

def mode_screen():
    root = tk.Tk()
    root.title("Wähle deinen Modus")
    root.geometry("800x600")
    root.configure(bg="#2e2e2e")  # Standard-Hintergrundfarbe

    # Schriftarten und Farben
    label_font = ("Helvetica", 16, "bold")
    btn_font = ("Helvetica", 14, "bold")
    btn_bg = "#444444"  # Dunkleres Grau für Buttons
    btn_fg = "#DDDDDD"  # Hellgrauer Text

    # Frame zum vollständigen Zentrieren
    frame = tk.Frame(root, bg="#2e2e2e")
    frame.place(relx=0.5, rely=0.5, anchor="center")

    # Modus-Auswahl Label
    tk.Label(frame, text="Wählen Sie den Spielmodus", font=label_font, fg="white", bg="#2e2e2e").pack(pady=20)

    # Buttons für Spielmodi
    btn_singleplayer = tk.Button(
        frame,
        text="🎮 Singleplayer",
        font=btn_font,
        bg=btn_bg,
        fg=btn_fg,
        relief="flat",
        command=lambda: start_game_mode("Singleplayer")  # Ruft den Singleplayer-Modus auf
    )
    btn_singleplayer.pack(pady=30, ipadx=40, ipady=20)

    btn_multiplayer = tk.Button(
        frame,
        text="🤝 Multiplayer",
        font=btn_font,
        bg=btn_bg,
        fg=btn_fg,
        relief="flat",
        command=lambda: start_game_mode("Multiplayer")  # Ruft den Multiplayer-Modus auf
    )
    btn_multiplayer.pack(pady=30, ipadx=40, ipady=20)

    root.mainloop()