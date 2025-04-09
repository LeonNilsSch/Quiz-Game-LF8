import sqlite3
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from repositories.question_repository import QuestionRepository
from repositories.category_repository import CategoryRepository


class AdminTool:
    def __init__(self):
        self.db_path = "Database/database.db"
        self.connection = sqlite3.connect(self.db_path)
        self.question_repo = QuestionRepository(self.connection)
        self.category_repo = CategoryRepository(self.connection)  # Initialisierung von category_repo

        self.root = tk.Tk()
        self.root.title("Admin Tool - Fragenverwaltung")
        self.root.geometry("800x700")
        self.root.configure(bg="#2e2e2e")

        # Frames für verschiedene Ansichten
        self.frames = {}
        self.create_frames()

        # Start mit der Frage-ID-Ansicht
        self.show_frame("question_id_frame")

        self.root.mainloop()

    def create_frames(self):
        """Erstellt alle Frames und speichert sie in einem Dictionary."""
        self.frames["question_id_frame"] = self.create_question_id_frame()
        self.frames["question_update_frame"] = self.create_question_update_frame()
        self.frames["answers_update_frame"] = self.create_answers_update_frame()
        self.frames["create_question_frame"] = self.create_question_frame()
        self.frames["create_question_text_frame"] = self.create_question_text_frame()
        self.frames["create_question_answers_frame"] = self.create_question_answers_frame()
        self.frames["create_question_category_frame"] = self.create_question_category_frame()

    def show_frame(self, frame_name):
        """Zeigt den gewünschten Frame an und versteckt alle anderen."""
        for name, frame in self.frames.items():
            if name == frame_name:
                frame.pack(fill="both", expand=True)
            else:
                frame.pack_forget()

    def create_question_id_frame(self):
        frame = tk.Frame(self.root, bg="#2e2e2e")
        tk.Label(
            frame,
            text="Frage-ID eingeben:",
            font=("Helvetica", 14),
            fg="white",
            bg="#2e2e2e",
        ).pack(pady=20)
        self.question_id_entry = tk.Entry(frame, font=("Helvetica", 14))
        self.question_id_entry.pack(pady=10)
        tk.Button(
            frame,
            text="Frage laden",
            font=("Helvetica", 14, "bold"),
            bg="#444444",
            fg="#DDDDDD",
            relief="flat",
            command=self.load_question,
        ).pack(pady=10, ipadx=20, ipady=10)
        tk.Button(
            frame,
            text="Frage löschen",
            font=("Helvetica", 14, "bold"),
            bg="#444444",
            fg="#DDDDDD",
            relief="flat",
            command=self.delete_question_confirmation,
        ).pack(pady=10, ipadx=20, ipady=10)
        tk.Button(
            frame,
            text="Frage erstellen",
            font=("Helvetica", 14, "bold"),
            bg="#444444",
            fg="#DDDDDD",
            relief="flat",
            command=lambda: self.show_frame("create_question_text_frame"),
        ).pack(pady=10, ipadx=20, ipady=10)
        return frame

    def create_question_update_frame(self):
        frame = tk.Frame(self.root, bg="#2e2e2e")
        tk.Label(
            frame,
            text="Fragetext aktualisieren:",
            font=("Helvetica", 14),
            fg="white",
            bg="#2e2e2e",
        ).pack(pady=20)
        self.question_text_entry = tk.Entry(frame, font=("Helvetica", 14), width=50)
        self.question_text_entry.pack(pady=10)
        tk.Button(
            frame,
            text="Weiter zu Antworten",
            font=("Helvetica", 14, "bold"),
            bg="#444444",
            fg="#DDDDDD",
            relief="flat",
            command=self.switch_to_answers_update_frame,
        ).pack(pady=20, ipadx=20, ipady=10)
        return frame

    def create_answers_update_frame(self):
        frame = tk.Frame(self.root, bg="#2e2e2e")
        tk.Label(
            frame,
            text="Antworten aktualisieren:",
            font=("Helvetica", 14),
            fg="white",
            bg="#2e2e2e",
        ).pack(pady=20)

        self.answer_entries = []
        self.correct_answer_var = tk.IntVar(value=0)

        for i in range(4):  # Platzhalter für 4 Antworten
            tk.Label(
                frame,
                text=f"Antwort {i + 1}:",
                font=("Helvetica", 14),
                fg="white",
                bg="#2e2e2e",
            ).pack(pady=5)
            entry = tk.Entry(frame, font=("Helvetica", 14), width=50)
            entry.pack(pady=5)
            self.answer_entries.append(entry)

            tk.Radiobutton(
                frame,
                text="Korrekte Antwort",
                variable=self.correct_answer_var,
                value=i + 1,
                bg="#2e2e2e",
                fg="white",
                selectcolor="#444444",
                font=("Helvetica", 12),
            ).pack(pady=5)

        tk.Button(
            frame,
            text="Frage aktualisieren",
            font=("Helvetica", 14, "bold"),
            bg="#444444",
            fg="#DDDDDD",
            relief="flat",
            command=self.update_question,
        ).pack(pady=20, ipadx=20, ipady=10)
        return frame

    def get_categories(self):
        """Gibt eine Liste von festen Kategorien zurück."""
        # Beispielhafte Kategorien mit festen IDs
        return {
            1: "Geografie",
            2: "Geschichte",
            3: "Wissenschaft",
            4: "Unterhaltung",
            5: "Sport"
        }

    def create_question_frame(self):
        """Erstellt das Frame für die Eingabe der Frage."""
        frame = tk.Frame(self.root, bg="#2e2e2e")

        # Fragetext
        tk.Label(frame, text="Fragetext:", bg="#2e2e2e", fg="white").pack(pady=5)
        self.new_question_entry = tk.Entry(frame, width=50)
        self.new_question_entry.pack(pady=5)

        # Kategorie-Auswahl
        tk.Label(frame, text="Kategorie:", bg="#2e2e2e", fg="white").pack(pady=5)
        self.category_combobox = ttk.Combobox(frame, values=self.category_repo.Get_category_name(), state="readonly")
        self.category_combobox.pack(pady=5)

        # Schwierigkeits-Auswahl
        tk.Label(frame, text="Schwierigkeit:", bg="#2e2e2e", fg="white").pack(pady=5)
        self.difficulty_combobox = ttk.Combobox(frame, values=self.get_difficulties(), state="readonly")
        self.difficulty_combobox.pack(pady=5)

        # Button zum Erstellen der Frage
        tk.Button(frame, text="Frage erstellen", command=self.create_new_question).pack(pady=20)

        return frame

    def create_new_question(self):
        """Erstellt eine neue Frage und speichert sie in der Datenbank."""
        try:
            # Fragetext abrufen
            question_text = self.new_question_entry.get().strip()

            # Antworten abrufen
            answers = [entry.get().strip() for entry in self.new_answers_entries]

            # Index der korrekten Antwort abrufen
            correct_answer_index = self.new_correct_answer_var.get()

            # Validierung
            if not question_text or not all(answers) or correct_answer_index == 0:
                messagebox.showerror("Fehler", "Bitte füllen Sie alle Felder aus und wählen Sie eine korrekte Antwort.")
                return

            # Aufruf der Repository-Methode zum Erstellen der Frage
            self.question_repo.Create_question(  # Großes "C" hier
                question=question_text,
                category_id=None,  # Kategorie wird nicht verwendet
                difficulty_id=None,  # Schwierigkeit wird nicht verwendet
                correct_answer=answers[correct_answer_index - 1],
                incorrect_answer1=answers[0] if correct_answer_index != 1 else answers[1],
                incorrect_answer2=answers[1] if correct_answer_index != 2 else answers[2],
                incorrect_answer3=answers[2] if correct_answer_index != 3 else answers[3],
            )

            # Erfolgsmeldung
            messagebox.showinfo("Erfolg", "Die Frage wurde erfolgreich erstellt.")
            self.show_frame("question_id_frame")

        except Exception as e:
            messagebox.showerror("Fehler", f"Fehler beim Erstellen der Frage: {e}")

    def get_category_id_by_name(self, category_name):
        """Holt die Kategorie-ID basierend auf dem Kategorienamen."""
        self.cursor.execute("SELECT categoryID FROM Category WHERE categoryName = ?", (category_name,))
        row = self.cursor.fetchone()
        return row[0] if row else None

    def get_difficulties(self):
        """Holt die Schwierigkeitsnamen aus der Datenbank."""
        self.cursor.execute("SELECT difficultyName FROM Difficulty")
        rows = self.cursor.fetchall()
        return [row[0] for row in rows]

    def get_difficulty_id_by_name(self, difficulty_name):
        """Holt die Schwierigkeit-ID basierend auf dem Schwierigkeitsnamen."""
        self.cursor.execute("SELECT difficultyID FROM Difficulty WHERE difficultyName = ?", (difficulty_name,))
        row = self.cursor.fetchone()
        return row[0] if row else None

    def load_question(self):
        try:
            question_id = int(self.question_id_entry.get())
            question = self.question_repo.Get_question_by_id(question_id)
            if not question:
                messagebox.showerror("Fehler", "Frage-ID nicht gefunden.")
                return

            # Fragetext in das Eingabefeld einfügen
            self.question_text_entry.delete(0, tk.END)
            self.question_text_entry.insert(0, question["questionText"])

            # Antworten in die Eingabefelder einfügen
            for i, answer in enumerate(question["answers"]):
                self.answer_entries[i].delete(0, tk.END)
                self.answer_entries[i].insert(0, answer["answerText"])

            # Korrekte Antwort setzen
            self.correct_answer_var.set(question["correctAnswerIndex"])

            self.show_frame("question_update_frame")
        except Exception as e:
            messagebox.showerror("Fehler", f"Fehler beim Laden der Frage: {e}")

    def switch_to_answers_update_frame(self):
        self.show_frame("answers_update_frame")

    def update_question(self):
        """Aktualisiert eine bestehende Frage in der Datenbank."""
        try:
            # Frage-ID und Fragetext abrufen
            question_id = int(self.question_id_entry.get())
            question_text = self.question_text_entry.get()

            # Antworten aus den Eingabefeldern abrufen
            answers = [entry.get() for entry in self.answer_entries]

            # Index der korrekten Antwort abrufen
            correct_answer_index = self.correct_answer_var.get()

            # Validierung: Sicherstellen, dass eine korrekte Antwort ausgewählt wurde
            if correct_answer_index == 0:
                messagebox.showerror("Fehler", "Bitte wählen Sie eine korrekte Antwort aus.")
                return

            # Aufruf der Repository-Methode zum Aktualisieren der Frage
            self.question_repo.update_question(
                questionID=question_id,
                questionText=question_text,
                answers=answers,
                correctAnswerIndex=correct_answer_index,
            )

            # Erfolgsmeldung anzeigen und zurück zur Frage-ID-Ansicht wechseln
            messagebox.showinfo("Erfolg", "Frage und Antworten wurden aktualisiert.")
            self.show_frame("question_id_frame")

        except Exception as e:
            # Fehlerbehandlung
            messagebox.showerror("Fehler", f"Fehler beim Aktualisieren: {e}")

    def delete_question_confirmation(self):
        """Zeigt ein Bestätigungsdialog zum Löschen der Frage."""
        question_id = self.question_id_entry.get()
        if not question_id.isdigit():
            messagebox.showerror("Fehler", "Bitte geben Sie eine gültige Frage-ID ein.")
            return

        confirm = messagebox.askyesno(
            "Frage löschen",
            f"Sind Sie sicher, dass Sie die Frage mit der ID {question_id} löschen möchten?",
        )
        if confirm:
            self.Delete_question(int(question_id))

    def Delete_question(self, question_id):
        """Löscht die Frage aus der Question-Tabelle."""
        try:
            # Aufruf der Repository-Methode zum Löschen der Frage
            self.question_repo.delete_question(question_id)
            messagebox.showinfo("Erfolg", f"Frage mit der ID {question_id} wurde gelöscht.")
            self.show_frame("question_id_frame")
        except Exception as e:
            messagebox.showerror("Fehler", f"Fehler beim Löschen der Frage: {e}")

    def create_question_text_frame(self):
        """Erstellt das Frame für die Eingabe des Fragetexts."""
        frame = tk.Frame(self.root, bg="#2e2e2e")

        tk.Label(
            frame,
            text="Fragetext eingeben:",
            font=("Helvetica", 16, "bold"),
            fg="white",
            bg="#2e2e2e",
        ).pack(pady=20)

        self.new_question_entry = tk.Entry(frame, font=("Helvetica", 14), width=50)
        self.new_question_entry.pack(pady=10)

        tk.Button(
            frame,
            text="Weiter zu Antworten",
            font=("Helvetica", 14, "bold"),
            bg="#444444",
            fg="#DDDDDD",
            relief="flat",
            command=self.switch_to_answers_frame,
        ).pack(pady=20, ipadx=20, ipady=10)

        return frame


    def create_question_answers_frame(self):
        """Erstellt das Frame für die Eingabe der Antworten."""
        frame = tk.Frame(self.root, bg="#2e2e2e")

        tk.Label(
            frame,
            text="Antworten eingeben:",
            font=("Helvetica", 16, "bold"),
            fg="white",
            bg="#2e2e2e",
        ).pack(pady=20)

        self.new_answers_entries = []
        self.new_correct_answer_var = tk.IntVar(value=0)

        for i in range(4):
            tk.Label(
                frame,
                text=f"Antwort {i + 1}:",
                font=("Helvetica", 14),
                fg="white",
                bg="#2e2e2e",
            ).pack(pady=5)
            entry = tk.Entry(frame, font=("Helvetica", 14), width=50)
            entry.pack(pady=5)
            self.new_answers_entries.append(entry)

            tk.Radiobutton(
                frame,
                text=f"Korrekte Antwort {i + 1}",
                variable=self.new_correct_answer_var,
                value=i + 1,
                bg="#2e2e2e",
                fg="white",
                selectcolor="#444444",
                font=("Helvetica", 12),
            ).pack(pady=5)

        tk.Button(
            frame,
            text="Weiter zu Kategorie und Schwierigkeit",
            font=("Helvetica", 14, "bold"),
            bg="#444444",
            fg="#DDDDDD",
            relief="flat",
            command=self.switch_to_category_frame,
        ).pack(pady=20, ipadx=20, ipady=10)

        return frame


    def create_question_category_frame(self):
        """Erstellt das Frame für die Auswahl von Kategorie und Schwierigkeit."""
        frame = tk.Frame(self.root, bg="#2e2e2e")

        tk.Label(
            frame,
            text="Kategorie und Schwierigkeit auswählen:",
            font=("Helvetica", 16, "bold"),
            fg="white",
            bg="#2e2e2e",
        ).pack(pady=20)

        # Kategorie auswählen
        tk.Label(
            frame,
            text="Kategorie:",
            font=("Helvetica", 14),
            fg="white",
            bg="#2e2e2e",
        ).pack(pady=5)
        self.new_category_var = tk.IntVar()
        categories = self.get_categories()
        for category_id, category_name in categories.items():
            tk.Radiobutton(
                frame,
                text=f"{category_name} (ID: {category_id})",
                variable=self.new_category_var,
                value=category_id,
                bg="#2e2e2e",
                fg="white",
                selectcolor="#444444",
                font=("Helvetica", 12),
            ).pack(pady=5)

        # Schwierigkeit auswählen
        tk.Label(
            frame,
            text="Schwierigkeit:",
            font=("Helvetica", 14),
            fg="white",
            bg="#2e2e2e",
        ).pack(pady=5)
        self.new_difficulty_var = tk.IntVar()
        difficulties = {1: "Leicht", 2: "Mittel", 3: "Schwer"}
        for difficulty_id, difficulty_name in difficulties.items():
            tk.Radiobutton(
                frame,
                text=f"{difficulty_name} (ID: {difficulty_id})",
                variable=self.new_difficulty_var,
                value=difficulty_id,
                bg="#2e2e2e",
                fg="white",
                selectcolor="#444444",
                font=("Helvetica", 12),
            ).pack(pady=5)

        tk.Button(
            frame,
            text="Frage erstellen",
            font=("Helvetica", 14, "bold"),
            bg="#444444",
            fg="#DDDDDD",
            relief="flat",
            command=self.create_new_question,
        ).pack(pady=20, ipadx=20, ipady=10)

        return frame


    def switch_to_answers_frame(self):
        """Wechselt zur Ansicht für die Eingabe der Antworten."""
        self.show_frame("create_question_answers_frame")


    def switch_to_category_frame(self):
        """Wechselt zur Ansicht für die Auswahl von Kategorie und Schwierigkeit."""
        self.show_frame("create_question_category_frame")
    

if __name__ == "__main__":
    AdminTool()