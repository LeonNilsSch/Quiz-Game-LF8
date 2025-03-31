import sqlite3
import random

# all SQL-Statements for question
class QuestionRepository:
    def __init__(self, db ="database.db"):
        self.con = sqlite3.connect(db)
        self.cursor = self.con.cursor()

    def get_questionIDs_with_Categorys(self, categoryid):
        # SQL-Abfrage to fetch question IDs by category
        self.cursor.execute(""" 
        SELECT 
            q.questionID
        FROM 
            Question q
        JOIN 
            Category c ON q.categoryID = c.categoryID
        WHERE
            c.categoryID = ?
        """, (categoryid,))
        
        # Ergebnisse holen und ausgeben
        rows = self.cursor.fetchall()
        return [row[0] for row in rows]  # Extract questionID from each row

    def fill_game_question(self, questionids, gameid):
        for i in questionids:
            self.cursor.execute(""" 
            INSERT INTO Game_Question(gameID, questionID, played) VALUES (?, ?, 0)
            """, (gameid, i,))
        self.con.commit()   
    
    def get_random_questionID(self, gameID):
        self.cursor.execute(""" 
        SELECT questionID FROM Game_Question WHERE played = 0 AND gameID = ?
        """, (gameID,))
        rows = self.cursor.fetchall()
        
        if rows:  # Ensure there are rows before trying to get a random ID
            ids = [row[0] for row in rows]  # Extract questionID from each row
            return random.choice(ids)
        else:
            return None  # Return None if no questions are available

    def get_question(self, questionID):
        self.cursor.execute(""" 
        SELECT * FROM Question WHERE questionID = ?
        """, (questionID,))
        rows = self.cursor.fetchall()
        
        # Return the first row (question details)
        if rows:
            return rows[0]
        else:
            return None  # If no question found, return None

    def get_correct_answer(self, questionID):
        self.cursor.execute(""" 
        SELECT correct_answer FROM Question WHERE questionID = ?
        """, (questionID,))
        rows = self.cursor.fetchall()
        
        if rows:
            return rows[0][0]  # Return the correct answer
        else:
            return None  # Return None if no correct answer found

    def create_question(self,question,categoryID,difficultyID,correct_answer,incorrect_answer1,incorrect_answer2,incorrect_answer3):
        self.cursor.execute(""" 
        INSERT INTO Question(question,categoryID,difficultyID,correct_answer,incorrect_answer1,incorrect_answer2,incorrect_answer3) 
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (question, categoryID, difficultyID, correct_answer, incorrect_answer1, incorrect_answer2, incorrect_answer3))
        self.con.commit()   
        
        return "Question created! :)"
        # Add logic here for creating a new question, for now just a placeholder
    