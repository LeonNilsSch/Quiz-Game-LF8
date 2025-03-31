import tkinter as tk
from tkinter import messagebox
import sqlite3
from selectionscreen import mode_screen  # Importiere den Auswahlmodus-Bildschirm

# Login-Funktion
def login(start_game_callback):
    username = entry_username.get()
    password = entry_password.get()

    # Datenbankverbindung für Login
    con = sqlite3.connect("./Database/database.db")
    cursor = con.cursor()

    cursor.execute("SELECT * FROM Player WHERE Playername = ? AND playerPassword = ?", (username, password))
    user = cursor.fetchone()
    con.close()

    if user:
        messagebox.showinfo("Erfolg", f"Login erfolgreich! Willkommen, {username}.")
        open_selection_screen()  # Öffnet den Auswahlmodus nach erfolgreichem Login
    else:
        messagebox.showerror("Fehler", "Falscher Benutzername oder Passwort.")

# Funktion, um den Auswahlmodus zu öffnen
def open_selection_screen():
    # Öffnet die Mode Selection GUI
    login_screen_window.destroy()  # Schließt das Login-Fenster
    mode_screen()  # Öffnet die Auswahlmodus-GUI

# Login-GUI
def login_screen(start_game_callback):
    global entry_username, entry_password, login_screen_window

    login_screen_window = tk.Tk()  # Erstelle das Login-Fenster
    login_screen_window.title("Login System")
    login_screen_window.geometry("800x600")
    login_screen_window.configure(bg="#2e2e2e")

    # Styling
    label_font = ("Helvetica", 12, "bold")
    entry_bg = "#333"
    entry_fg = "white"
    btn_bg = "#6e6e6e"
    btn_fg = "white"
    btn_hover_bg = "#1e1e1e"
    btn_border_width = 0

    # Frame zum vollständigen Zentrieren
    frame = tk.Frame(login_screen_window, bg="#2e2e2e")
    frame.place(relx=0.5, rely=0.5, anchor="center")  # Frame exakt in der Mitte platzieren

    # Benutzername
    tk.Label(frame, text="Benutzername:", font=label_font, fg="white", bg="#2e2e2e").pack(pady=5)
    entry_username = tk.Entry(frame, font=label_font, bg=entry_bg, fg=entry_fg)
    entry_username.pack(pady=5)

    # Passwort
    tk.Label(frame, text="Passwort:", font=label_font, fg="white", bg="#2e2e2e").pack(pady=5)
    entry_password = tk.Entry(frame, font=label_font, bg=entry_bg, fg=entry_fg, show="*")
    entry_password.pack(pady=5)

    # Login-Button
    btn_login = tk.Button(frame, text="Login", font=label_font, bg=btn_bg, fg=btn_fg, relief="flat", bd=btn_border_width, command=lambda: login(start_game_callback))
    btn_login.pack(pady=10, ipadx=20, ipady=10)

    # Button Hover-Effekt
    def on_enter(event, button):
        button.config(bg=btn_hover_bg)

    def on_leave(event, button):
        button.config(bg=btn_bg)

    btn_login.bind("<Enter>", lambda event, button=btn_login: on_enter(event, button))
    btn_login.bind("<Leave>", lambda event, button=btn_login: on_leave(event, button))

    login_screen_window.mainloop()
