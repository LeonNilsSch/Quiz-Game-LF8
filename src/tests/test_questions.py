import unittest
import sqlite3
import os
from repositories.question_repository import QuestionRepository

class TestQuestionsRepository(unittest.TestCase):
    def setUp(self):
        """Erstellt eine temporäre In-Memory SQLite-Datenbank für den Test."""
        self.conn = sqlite3.connect(":memory:")  # In-Memory-DB
        self.cursor = self.conn.cursor()

        # Tabelle manuell erstellen
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Question (
                questionID INTEGER PRIMARY KEY AUTOINCREMENT,
                categoryID INTEGER,
                difficultyID INTEGER,
                question TEXT UNIQUE NOT NULL,
                correctAnswer TEXT NOT NULL,
                incorrectAnswers1 TEXT NOT NULL,
                incorrectAnswers2 TEXT NOT NULL,
                incorrectAnswers3 TEXT NOT NULL
            );
        """)
        self.conn.commit()

        # Repository nutzt jetzt die in-memory DB über die Verbindung
        self.questions = QuestionRepository(connection=self.conn)

    def test_create_question(self):
        new_question = "Was ist die Hauptstadt von Deutschland?"
        self.questions.create_question(new_question, 1, 1, "Berlin", "Hamburg", "München", "Bielefeld")

        # Überprüfe, ob die Frage in der Datenbank vorhanden ist
        self.cursor.execute("SELECT question FROM Question WHERE question = ?", (new_question,))
        result = self.cursor.fetchone()

        self.assertIsNotNone(result)
        self.assertEqual(result[0], new_question)

    def tearDown(self):
        self.conn.close()

if __name__ == '__main__':
    unittest.main()
