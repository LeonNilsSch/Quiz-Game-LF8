import sqlite3
import random

# Assuming database connection is established here
con = sqlite3.connect("database.db")
cursor = con.cursor()

class Question:
    def __init__(self, question_text: str, options: list, correct_answer: str, category: str):
        self.question_text = question_text
        self.options = options
        self.correct_answer = correct_answer
        self.category = category

    def get_questionIDs_with_Categorys(self, category):
        # SQL-Abfrage to fetch question IDs by category
        cursor.execute(""" 
        SELECT 
            q.questionID
        FROM 
            Question q
        JOIN 
            Category c ON q.categoryID = c.categoryID
        WHERE
            c.name = ?
        """, (category,))
        
        # Ergebnisse holen und ausgeben
        rows = cursor.fetchall()
        return [row[0] for row in rows]  # Extract questionID from each row

    def fill_game_question(self, questionids, gameid):
        for i in questionids:
            cursor.execute(""" 
            INSERT INTO Game_Question(gameID, questionID, played) VALUES (?, ?, 0)
            """, (gameid, i,))
        con.commit()   
    
    def get_random_questionID(self, gameID):
        cursor.execute(""" 
        SELECT questionID FROM Game_Question WHERE played = 0 AND gameID = ?
        """, (gameID,))
        rows = cursor.fetchall()
        
        if rows:  # Ensure there are rows before trying to get a random ID
            ids = [row[0] for row in rows]  # Extract questionID from each row
            return random.choice(ids)
        else:
            return None  # Return None if no questions are available

    def get_question(self, gameID, questionID):
        cursor.execute(""" 
        SELECT * FROM Question WHERE questionID = ?
        """, (questionID,))
        rows = cursor.fetchall()
        
        # Return the first row (question details)
        if rows:
            return rows[0]
        else:
            return None  # If no question found, return None

    def get_correct_answer(self, questionID):
        cursor.execute(""" 
        SELECT correct_answer FROM Question WHERE questionID = ?
        """, (questionID,))
        rows = cursor.fetchall()
        
        if rows:
            return rows[0][0]  # Return the correct answer
        else:
            return None  # Return None if no correct answer found

    def create_question(self):
        # Add logic here for creating a new question, for now just a placeholder
        pass