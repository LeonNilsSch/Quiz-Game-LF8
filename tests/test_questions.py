import unittest
import sqlite3
from repositories.question_repository import QuestionRepository

class TestQuestionsRepository(unittest.TestCase):
    def setUp(self):
        """Erstellt eine temporäre In-Memory SQLite-Datenbank für jeden Test."""
        self.conn = sqlite3.connect(":memory:")  # Temporäre Datenbank
        self.cursor = self.conn.cursor()

        # Erstelle die Tabelle für Fragen (angepasst an deine Schema)
        self.cursor.execute("""
                            CREATE TABLE IF NOT EXISTS Question (
                            questionID INTEGER PRIMARY KEY AUTOINCREMENT,
                            categoryID INTEGER,
                            difficultyID INTEGER,
                            question TEXT UNIQUE NOT NULL,
                            correctAnswer TEXT NOT NULL,
                            incorrectAnswers1 TEXT NOT NULL,
                            incorrectAnswers2 TEXT NOT NULL,
                            incorrectAnswers3 TEXT NOT NULL,
                            FOREIGN KEY (categoryID) REFERENCES Category(categoryID),
                            FOREIGN KEY (difficultyID) REFERENCES Difficulty(difficultyID)
                            );
                            """)
        self.conn.commit()

        # Erstelle eine Instanz von Questions mit dieser Test-Datenbank
        self.questions = QuestionRepository(self.conn)

    # def test_get_question(self):
    #     # Testet, ob get_question() eine nicht-leere Zeichenkette zurückgibt
    #     question = self.questions.get_question()
    #     self.assertIsInstance(question, str)
    #     self.assertTrue(len(question) > 0)

    def test_create_question(self):
        #givene
        """Testet, ob eine Frage erfolgreich hinzugefügt werden kann."""
        new_question = "Was ist die Hauptstadt von Deutschland?"

        #when
        # Hier rufst du einfach die Methode auf, die den SQL-Befehl enthält
        self.questions.create_question(new_question, 1, 1, "Berlin", "Hamburg", "München", "Bielefeld")
        
        
        # Überprüfe, ob die Frage in der Datenbank ist
        self.cursor.execute("SELECT question FROM Question WHERE question = ?", (new_question,))
        result = self.cursor.fetchone()
        
        #then
        self.assertIsNotNone(result)  # Prüfen, ob die Frage existiert
        self.assertEqual(result[0], new_question)        


    def test_remove_question(self):
        # Testet, ob eine Frage erfolgreich entfernt wird
        questionID = 1
        self.questions.delete_question(questionID)
        self.assertIsNone(self.questions.get_question(questionID))

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestQuestionsRepository("test_create_question"))
    suite.addTest(TestQuestionsRepository("test_remove_question"))
    
    runner = unittest.TextTestRunner()
    runner.run(suite)

