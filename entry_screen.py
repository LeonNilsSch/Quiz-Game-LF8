import tkinter as tk
from login import login_screen  # Importiere die Login-GUI

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
main_screen.configure(bg="#2e2e2e")  # Hintergrundfarbe angepasst

# Styling
label_font = ("Helvetica", 16, "bold")
btn_font = ("Helvetica", 14, "bold")
btn_bg = "#6e6e6e"
btn_fg = "white"
btn_hover_bg = "#1e1e1e"
btn_border_width = 0

# Frame zum Zentrieren des Inhalts
frame = tk.Frame(main_screen, bg="#2e2e2e")
frame.pack(expand=True, fill="both")

# Innerer Frame zum Mitten Ausrichten
inner_frame = tk.Frame(frame, bg="#2e2e2e")
inner_frame.place(relx=0.5, rely=0.5, anchor="center")

# Titel-Label
tk.Label(inner_frame, text="Willkommen zum Quiz-Game", font=label_font, fg="white", bg="#2e2e2e").pack(pady=20)

# Spielen-Button
btn_play = tk.Button(inner_frame, text="Spielen", font=btn_font, bg=btn_bg, fg=btn_fg, relief="flat", bd=btn_border_width, command=open_login)
btn_play.pack(pady=20, ipadx=20, ipady=10)

# Button Hover-Effekt
def on_enter(event, button):
    button.config(bg=btn_hover_bg)

def on_leave(event, button):
    button.config(bg=btn_bg)

btn_play.bind("<Enter>", lambda event, button=btn_play: on_enter(event, button))
btn_play.bind("<Leave>", lambda event, button=btn_play: on_leave(event, button))

# Start der GUI
main_screen.mainloop()
