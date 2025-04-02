import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from selection_screen import mode_screen  # Richtiger Name

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

    # Schriftarten und Farben
    label_font = ("Helvetica", 16, "bold")  # Moderne Schriftart
    entry_bg = "#3E3E3E"  # Dunkles Grau für das Eingabefeld
    entry_fg = "#FFFFFF"  # Weißer Text für gute Lesbarkeit
    btn_font = ("Helvetica", 14, "bold")  # Button-Schriftart

    # Frame zum vollständigen Zentrieren
    frame = ttk.Frame(login_screen_window, padding=20, style="Custom.TFrame")
    frame.place(relx=0.5, rely=0.5, anchor="center")  # Frame exakt in der Mitte platzieren

    # Benutzername
    ttk.Label(frame, text="Benutzername:", font=label_font).pack(pady=5)
    entry_username = ttk.Entry(frame, font=label_font, background=entry_bg, foreground=entry_fg)
    entry_username.pack(pady=5)

    # Passwort
    ttk.Label(frame, text="Passwort:", font=label_font).pack(pady=5)
    entry_password = ttk.Entry(frame, font=label_font, background=entry_bg, foreground=entry_fg, show="*")
    entry_password.pack(pady=5)

    # Button-Stil konfigurieren (identisch zu Entry Screen)
    style = ttk.Style()
    style.configure("Custom.TButton", background="#222222", foreground="#FFFFFF", borderwidth=1)
    style.map("Custom.TButton", background=[("active", "#333333")])

    # Login-Button
    btn_login = ttk.Button(frame, text="Login", command=lambda: login(start_game_callback), style="Custom.TButton")
    btn_login.pack(pady=10, ipadx=20, ipady=10)

    login_screen_window.mainloop()