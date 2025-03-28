import sqlite3
import tkinter as tk
from tkinter import messagebox
from login import login_screen
from question import Question

# Funktion zum Starten des Spiels nach erfolgreichem Login
def start_game():
    # Verbindung zur Datenbank herstellen
    con = sqlite3.connect("database.db")
    
    # Create a new question object and pass the connection
    q = Question("Sample question", ["Option1", "Option2"], "Option1", "Politics", con)
    
    # Get question IDs based on the category
    ids = q.get_questionIDs_with_Categorys("Politics")  # Example category
    q.fill_game_question(ids, 1)
    
    # Get a random question ID
    questionid = q.get_random_questionID(1)
    
    # Get the question based on the ID
    question = q.get_question(1, questionid)
    
    # Get the correct answer
    correct_answer = q.get_correct_answer(questionid)
    
    # For debugging purposes, print the question and correct answer
    print(f"Question: {question}")
    print(f"Correct Answer: {correct_answer}")
    
    # Now, transition to the selection screen after starting the game
    open_selection_screen()
    
    # Verbindung schließen
    con.commit()
    con.close()

# Funktion, um den Login-Screen anzuzeigen
def open_login():
    main_screen.destroy()  
    login_screen(start_game)

# Funktion, um den Auswahlbildschirm anzuzeigen
def open_selection_screen():
    # Implement selection screen logic or transition here
    print("Selection screen opened!")

# Hauptbildschirm (Entry Screen)
main_screen = tk.Tk()
main_screen.title("Willkommen zum Quiz-Game")
main_screen.geometry("800x600")
main_screen.configure(bg="#1e1e1e")

# Styling
label_font = ("Arial", 16, "bold")
btn_font = ("Arial", 14, "bold")
btn_bg = "#00BFFF"
btn_fg = "black"

# NEU: Frame zum Zentrieren des Inhalts (jetzt wirklich in der Mitte)
frame = tk.Frame(main_screen, bg="#1e1e1e")
frame.pack(expand=True, fill="both")  # Füllt das Fenster komplett aus

# NEU: Einen inneren Frame erstellen, der den Inhalt mittig hält
inner_frame = tk.Frame(frame, bg="#1e1e1e")
inner_frame.place(relx=0.5, rely=0.5, anchor="center")  # Absolut in die Mitte setzen

# Titel-Label (Innerhalb des inneren Frames)
tk.Label(inner_frame, text="Willkommen zum Quiz-Game", font=label_font, fg="white", bg="#1e1e1e").pack(pady=20)

# Spielen-Button (Innerhalb des inneren Frames)
btn_play = tk.Button(inner_frame, text="Spielen", font=btn_font, bg=btn_bg, fg=btn_fg, command=open_login)
btn_play.pack(pady=20)

# Start der GUI
main_screen.mainloop()