import tkinter as tk
from difficultyscreen import difficulty_screen  # Importiere die Funktion aus der difficultyscreen.py

# Funktion zum Starten des Spiels mit der Auswahl
def start_game_mode(mode):
    print(f"Spielmodus {mode} wurde ausgewählt!")
    choose_mode(mode)  # Rufe die Moduswahl-Funktion auf, um zum Schwierigkeitsbildschirm zu wechseln

# Funktion für die Auswahl des Modus
def choose_mode(mode):
    print(f"Ausgewählter Modus: {mode}")
    difficulty_screen()  # Öffnet den Schwierigkeitsauswahl-Bildschirm nach der Moduswahl

def mode_screen():
    root = tk.Tk()
    root.title("Wähle deinen Modus")
    root.geometry("800x600")
    root.configure(bg="#2e2e2e")

    # Styling
    label_font = ("Helvetica", 16, "bold")
    btn_font = ("Helvetica", 14, "bold")
    btn_bg = "#6e6e6e"
    btn_fg = "white"
    btn_hover_bg = "#1e1e1e"
    btn_border_width = 0

    # Frame zum vollständigen Zentrieren
    frame = tk.Frame(root, bg="#2e2e2e")
    frame.place(relx=0.5, rely=0.5, anchor="center")

    # Modus-Auswahl
    tk.Label(frame, text="Wählen Sie den Spielmodus", font=label_font, fg="white", bg="#2e2e2e").pack(pady=20)

    # Buttons für Spielmodi
    btn_singleplayer = tk.Button(frame, text="Singleplayer", font=btn_font, bg=btn_bg, fg=btn_fg, relief="flat", bd=btn_border_width, command=lambda: start_game_mode("Singleplayer"))
    btn_singleplayer.pack(pady=10, ipadx=20, ipady=10)

    btn_multiplayer = tk.Button(frame, text="Multiplayer", font=btn_font, bg=btn_bg, fg=btn_fg, relief="flat", bd=btn_border_width, command=lambda: start_game_mode("Multiplayer"))
    btn_multiplayer.pack(pady=10, ipadx=20, ipady=10)

    # Button Hover-Effekt
    def on_enter(event, button):
        button.config(bg=btn_hover_bg)

    def on_leave(event, button):
        button.config(bg=btn_bg)

    btn_singleplayer.bind("<Enter>", lambda event, button=btn_singleplayer: on_enter(event, button))
    btn_singleplayer.bind("<Leave>", lambda event, button=btn_singleplayer: on_leave(event, button))

    btn_multiplayer.bind("<Enter>", lambda event, button=btn_multiplayer: on_enter(event, button))
    btn_multiplayer.bind("<Leave>", lambda event, button=btn_multiplayer: on_leave(event, button))

    root.mainloop()
