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

        # Initialisiere das Hauptfenster
        self.root = tk.Tk()
        self.root.title("Quiz-Spiel")
        self.root.geometry("800x600")
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

    def load_next_question(self):
        if self.current_question_index >= len(self.question_ids):
            self.end_game()
            return

        question_id = self.question_ids[self.current_question_index]
        question_data = self.question_repo.get_question(question_id)

        # Extrahiere die Frage und Antworten
        question_text = question_data["question_text"]
        correct_answer = question_data["correct_answer"]
        incorrect_answers = [
            question_data["incorrect_answer1"],
            question_data["incorrect_answer2"],
            question_data["incorrect_answer3"]
        ]

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
                 f"Korrekte Antwort: {correct_answer}\n"
                 f"Falsche Antworten: {', '.join(incorrect_answers)}"
        )
        for i, option in enumerate(self.current_question.options):
            self.answer_buttons[i].config(text=option, state="normal")

        self.current_question_index += 1

    def check_answer(self, selected_index):
        selected_answer = self.current_question.options[selected_index]
        is_correct = self.current_question.right_or_wrong(selected_answer, self.current_question.correct_answer)

        if is_correct:
            self.score += 1
            messagebox.showinfo("Richtig!", "Das war die richtige Antwort!")
        else:
            messagebox.showerror("Falsch!", f"Die richtige Antwort war: {self.current_question.correct_answer}")

        # Aktualisiere den Punktestand
        self.score_label.config(text=f"Punkte: {self.score}")

        # Lade die nächste Frage
        self.load_next_question()

    def end_game(self):
        messagebox.showinfo("Spiel beendet", f"Das Spiel ist vorbei! Dein Punktestand: {self.score}")
        self.root.destroy()

# Beispielaufruf
if __name__ == "__main__":
    # Ersetze `1` durch die tatsächliche Kategorie-ID, die zuvor ausgewählt wurde
    GameplayScreen(category_id=1)