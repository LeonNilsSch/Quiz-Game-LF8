import sqlite3
import tkinter as tk
from tkinter import messagebox

# Login-Funktion
def login(start_game_callback):
    username = entry_username.get()
    password = entry_password.get()

    con = sqlite3.connect("database.db")
    cursor = con.cursor()

    cursor.execute("SELECT * FROM Player WHERE Playername = ? AND playerPassword = ?", (username, password))
    user = cursor.fetchone()
    con.close()

    if user:
        messagebox.showinfo("Erfolg", f"Login erfolgreich! Willkommen, {username}.")
        start_game_callback()  # Start the game and proceed to next screen
    else:
        messagebox.showerror("Fehler", "Falscher Benutzername oder Passwort.")

# Login-GUI
def login_screen(start_game_callback):
    global entry_username, entry_password

    root = tk.Tk()
    root.title("Login System")
    root.geometry("800x600")
    root.configure(bg="#1e1e1e")

    # Styling
    label_font = ("Arial", 12, "bold")
    entry_bg = "#333"
    entry_fg = "white"
    btn_bg = "#0078D7"
    btn_fg = "black"

    # Frame zum vollständigen Zentrieren
    frame = tk.Frame(root, bg="#1e1e1e")
    frame.place(relx=0.5, rely=0.5, anchor="center")  # Frame exakt in der Mitte platzieren

    # Benutzername
    tk.Label(frame, text="Benutzername:", font=label_font, fg="white", bg="#1e1e1e").pack(pady=5)
    entry_username = tk.Entry(frame, font=label_font, bg=entry_bg, fg=entry_fg)
    entry_username.pack(pady=5)

    # Passwort
    tk.Label(frame, text="Passwort:", font=label_font, fg="white", bg="#1e1e1e").pack(pady=5)
    entry_password = tk.Entry(frame, font=label_font, bg=entry_bg, fg=entry_fg, show="*")
    entry_password.pack(pady=5)

    # Login-Button
    btn_login = tk.Button(frame, text="Login", font=label_font, bg=btn_bg, fg=btn_fg, command=lambda: login(start_game_callback))
    btn_login.pack(pady=10)

    root.mainloop()