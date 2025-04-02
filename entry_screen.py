import tkinter as tk
from tkinter import ttk
from login_screen import login_screen  # Importiere die Login-GUI

# Funktion, die nach erfolgreichem Login das Spiel startet
def start_game():
    print("Spiel gestartet!")
    # Hier kannst du die nächste GUI für das Spiel oder die Modus-Auswahl öffnen

def open_login():
    main_screen.destroy()  # Zerstöre die Startseite
    login_screen(start_game)  # Übergibt start_game an die Login-GUI, damit sie nach Login ausgeführt wird

# Hauptbildschirm (Entry Screen)
main_screen = tk.Tk()
main_screen.title("Willkommen zum Quiz-Game")
main_screen.geometry("800x600")
main_screen.configure(bg="#1e1e1e")  # Noch dunkleres Grau für besseren Kontrast

# Globale Styles für macOS-Kompatibilität
main_screen.option_add('*TButton*background', '#222222')
main_screen.option_add('*TButton*foreground', '#FFFFFF')
main_screen.option_add('*TButton*borderwidth', 1)
main_screen.option_add('*TButton.padding', [10, 5])
main_screen.option_add('*TLabel*foreground', '#FFFFFF')
main_screen.option_add('*TLabel*background', '#1e1e1e')

# Schriftarten für Labels und Buttons
label_font = ("Helvetica", 16, "bold")  # Schriftart für Labels
btn_font = ("Helvetica", 14, "bold")  # Schriftart für Buttons

# Frame zum Zentrieren des Inhalts
frame = ttk.Frame(main_screen)
frame.pack(expand=True, fill="both")

# Innerer Frame zum Mitten Ausrichten
inner_frame = ttk.Frame(frame)
inner_frame.place(relx=0.5, rely=0.5, anchor="center")

# Titel-Label
ttk.Label(inner_frame, text="Willkommen zum Quiz-Game", font=label_font).pack(pady=20)

# Style für macOS anpassen (kein Hover-Effekt)
style = ttk.Style()
style.configure("Custom.TButton", background="#222222", foreground="#FFFFFF", borderwidth=1)

# Spielen-Button (jetzt statisch ohne Hover-Änderung)
btn_play = ttk.Button(inner_frame, text="Spielen", command=open_login, style="Custom.TButton")
btn_play.pack(pady=20, ipadx=20, ipady=1)

# Start der GUI
main_screen.mainloop()