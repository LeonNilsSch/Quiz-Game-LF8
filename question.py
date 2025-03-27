import sqlite3
import random
con = sqlite3.connect("database.db")
cursor = con.cursor()
        
class Question:
    def __init__(self, question_text: str, options: list, correct_answer: str, category: str):
        self.question_text = question_text
        self.options = options
        self.correct_answer = correct_answer
        self.category = category

    def get_questionID(self):
        # Verbindung zur Datenbank und Cursor erstellen
        
        # SQL-Abfrage
        cursor.execute(""" 
        SELECT 
            q.QuestionID,
            c.name
        FROM 
            Question q
        JOIN 
            Category c ON q.CategoryID = c.CategoryID
        WHERE
            c.name = "Politics"
        """)
        
        # Ergebnisse holen und ausgeben
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        
        # Verbindung schließen
        # con.commit()
        # con.close()