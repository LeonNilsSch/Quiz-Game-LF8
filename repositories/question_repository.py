import sqlite3
import random

class QuestionRepository:
    def __init__(self, db="Database/database.db"):
        # Prüfen, ob db eine Connection oder ein String-Pfad ist
        if isinstance(db, str):
            self.con = sqlite3.connect(db)
        else:
            self.con = db  # Falls schon eine Connection übergeben wurde

        self.cursor = self.con.cursor()

    def get_questionIDs_with_Categorys(self, categoryid):
        self.cursor.execute(""" 
        SELECT q.questionID
        FROM Question q
        JOIN Category c ON q.categoryID = c.categoryID
        WHERE c.categoryID = ?
        """, (categoryid,))
        
        rows = self.cursor.fetchall()
        return [row[0] for row in rows]

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
        
        if rows:
            ids = [row[0] for row in rows]
            return random.choice(ids)
        return None

    def get_question(self, questionID):
        self.cursor.execute(""" 
        SELECT * FROM Question WHERE questionID = ?
        """, (questionID,))
        rows = self.cursor.fetchall()
        
        return rows[0] if rows else None

    def get_correct_answer(self, questionID):
        self.cursor.execute(""" 
        SELECT correct_answer FROM Question WHERE questionID = ?
        """, (questionID,))
        rows = self.cursor.fetchall()
        
        return rows[0][0] if rows else None

    def create_question(self, question, categoryID, difficultyID, correct_answer, incorrect_answer1, incorrect_answer2, incorrect_answer3):
        self.cursor.execute(""" 
        INSERT INTO Question(question, categoryID, difficultyID, correct_answer, incorrect_answer1, incorrect_answer2, incorrect_answer3) 
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (question, categoryID, difficultyID, correct_answer, incorrect_answer1, incorrect_answer2, incorrect_answer3))
        self.con.commit()   
        
        return "Question created! :)"
    
    def fill_right_or_wrong(self,playerID,gameID,questionID,right:bool):
        self.cursor.execute("""
                                INSERT INTO right_or_wrong(playerID,gameID,questionID,right) VALUES(?,?,?,?)
                             """, (playerID,gameID,questionID,right))
        return
    
    def get_question_points(self,questionId):
        self.cursor.execute(""" 
        SELECT d.difficultyID, d.points
        FROM Difficulty d
        JOIN Question q ON d.difficultyID = q.difficultyID
        WHERE q.questionID = ?
        """, (questionId,))
        
        rows = self.cursor.fetchall()
        return [row[0] for row in rows]
    
    
