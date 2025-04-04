import sys
import os
import random

# Füge den Hauptordner `src` zum Python-Suchpfad hinzu
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

import tkinter as tk
from tkinter import messagebox
from src.question import Question
from repositories.question_repository import QuestionRepository

class GameplayScreen:
    def __init__(self, category_id):
        self.category_id = category_id
        self.question_repo = QuestionRepository()
        self.current_question = None
        self.score = 0
        self.question_ids = self.question_repo.get_questionIDs_with_Categorys(self.category_id)
        self.current_question_index = 0
        self.time_left = 10  # Timer in Sekunden

        # Initialisiere das Hauptfenster
        self.root = tk.Tk()
        self.root.title("Quiz-Spiel")
        self.root.geometry("1200x800")  # Breite x Höhe
        self.root.configure(bg="#2e2e2e")

        # Schriftarten und Farben
        self.label_font = ("Helvetica", 16, "bold")
        self.btn_font = ("Helvetica", 14, "bold")
        self.btn_bg = "#444444"
        self.btn_fg = "#DDDDDD"

        # GUI-Elemente erstellen
        self.create_widgets()

        # Erste Frage laden
        self.load_next_question()

        self.root.mainloop()

    def create_widgets(self):
        # Frame für die Frage
        self.question_frame = tk.Frame(self.root, bg="#2e2e2e")
        self.question_frame.pack(pady=20)

        self.question_label = tk.Label(
            self.question_frame, text="", font=self.label_font, fg="white", bg="#2e2e2e", wraplength=700
        )
        self.question_label.pack()

        # Frame für die Antwort-Buttons
        self.answer_frame = tk.Frame(self.root, bg="#2e2e2e")
        self.answer_frame.pack(pady=20)

        self.answer_buttons = []
        for i in range(4):  # Maximal 4 Antwortmöglichkeiten
            btn = tk.Button(
                self.answer_frame,
                text="",
                font=self.btn_font,
                bg=self.btn_bg,
                fg=self.btn_fg,
                relief="flat",
                command=lambda i=i: self.check_answer(i)
            )
            btn.pack(pady=5, ipadx=20, ipady=10, fill="x")
            self.answer_buttons.append(btn)

        # Frame für den Score
        self.score_label = tk.Label(
            self.root, text=f"Punkte: {self.score}", font=self.label_font, fg="white", bg="#2e2e2e"
        )
        self.score_label.pack(pady=20)

        # Timer-Label
        self.timer_label = tk.Label(
            self.root, text=f"Zeit: {self.time_left} Sekunden", font=self.label_font, fg="white", bg="#2e2e2e"
        )
        self.timer_label.pack(pady=20)

        # Label für Feedback (Richtig/Falsch)
        self.feedback_label = tk.Label(
            self.root, text="", font=self.label_font, fg="white", bg="#2e2e2e"
        )
        self.feedback_label.pack(pady=20)

    def load_next_question(self):
        if self.current_question_index >= len(self.question_ids):
            self.end_game()
            return

        question_id = self.question_ids[self.current_question_index]
        question_data = self.question_repo.get_question(question_id)

        # Debugging: Überprüfen, welche Schlüssel in question_data vorhanden sind
        print(f"Erhaltene Daten für Frage ID {question_id}: {question_data}")

        try:
            # Überprüfen und anpassen der Feldnamen
            question_text = question_data["questionText"]  # Beispiel: Anpassen an den tatsächlichen Spaltennamen
            correct_answer = question_data["correctAnswer"]  # Beispiel: Anpassen an den tatsächlichen Spaltennamen
            incorrect_answers = [
                question_data["incorrectAnswer1"],  # Beispiel: Anpassen an den tatsächlichen Spaltennamen
                question_data["incorrectAnswer2"],  # Beispiel: Anpassen an den tatsächlichen Spaltennamen
                question_data["incorrectAnswer3"]   # Beispiel: Anpassen an den tatsächlichen Spaltennamen
            ]
        except KeyError as e:
            print(f"Fehlender Schlüssel in den Daten: {e}")
            self.end_game()
            return

        # Mische die Antworten
        all_answers = [correct_answer] + incorrect_answers
        random.shuffle(all_answers)

        # Erstelle ein Question-Objekt
        self.current_question = Question(
            question_text=question_text,
            options=all_answers,
            correct_answer=correct_answer,
            category=self.category_id
        )

        # Frage und Antworten in der GUI anzeigen
        self.question_label.config(
            text=f"Frage ID: {question_id}\n\n{self.current_question.question_text}\n\n"
        )
        for i, option in enumerate(self.current_question.options):
            self.answer_buttons[i].config(text=option, state="normal")

        # Punkte für die aktuelle Frage holen
        question_points = self.question_repo.get_question_points(question_id)
        self.current_question_points = question_points[1] if question_points else 0

        self.current_question_index += 1

        # Timer zurücksetzen und starten
        self.time_left = 10
        self.update_timer()

    def update_timer(self):
        if self.time_left > 0:
            self.timer_label.config(text=f"Zeit: {self.time_left} Sekunden")
            self.time_left -= 1
            self.root.after(1000, self.update_timer)
        else:
            # Zeit abgelaufen
            self.end_game()

    def check_answer(self, selected_index):
        selected_answer = self.current_question.options[selected_index]
        is_correct = self.current_question.right_or_wrong(selected_answer, self.current_question.correct_answer)

        if is_correct:
            self.score += self.current_question_points
            self.feedback_label.config(text=f"Richtig! (+{self.current_question_points} Punkte)", fg="green")
        else:
            self.feedback_label.config(text=f"Falsch! Richtige Antwort: {self.current_question.correct_answer}", fg="red")

        # Aktualisiere den Punktestand
        self.score_label.config(text=f"Punkte: {self.score}")

        # Lade die nächste Frage nach kurzer Verzögerung
        self.root.after(2000, self.load_next_question)

    def end_game(self):
        # Entferne alle Widgets und zeige die Endpunktzahl
        for widget in self.root.winfo_children():
            widget.destroy()

        # Zeige die Punktzahl
        tk.Label(
            self.root, text=f"Spiel beendet! Deine Punktzahl: {self.score}", font=self.label_font, fg="white", bg="#2e2e2e"
        ).pack(pady=20)

        # Button zum Entry-Screen
        tk.Button(
            self.root,
            text="Zurück zum Hauptmenü",
            font=self.btn_font,
            bg=self.btn_bg,
            fg=self.btn_fg,
            relief="flat",
            command=self.return_to_entry_screen
        ).pack(pady=20, ipadx=20, ipady=10)

    def return_to_entry_screen(self):
        self.root.destroy()
        from GUI.entry_screen import entry_screen  # Importieren Sie die Funktion
        entry_screen()  # Starten Sie den Entry-Screen

# Beispielaufruf
if __name__ == "__main__":
    # Ersetze `1` durch die tatsächliche Kategorie-ID, die zuvor ausgewählt wurde
    GameplayScreen(category_id=1)