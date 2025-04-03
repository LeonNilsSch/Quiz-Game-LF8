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
        """
        Holt alle Frage-IDs für eine bestimmte Kategorie.
        """
        self.cursor.execute(""" 
        SELECT q.questionID
        FROM Question q
        JOIN Category c ON q.categoryID = c.categoryID
        WHERE c.categoryID = ?
        """, (categoryid,))
        
        rows = self.cursor.fetchall()
        return [row[0] for row in rows]

    def fill_game_question(self, questionids, gameid):
        """
        Füllt die Tabelle Game_Question mit den Frage-IDs für ein bestimmtes Spiel.
        """
        for i in questionids:
            self.cursor.execute(""" 
            INSERT INTO Game_Question(gameID, questionID, played) VALUES (?, ?, 0)
            """, (gameid, i,))
        self.con.commit()   

    def get_random_questionID(self, gameID):
        """
        Holt eine zufällige Frage-ID aus der Tabelle Game_Question, die noch nicht gespielt wurde.
        """
        self.cursor.execute(""" 
        SELECT questionID FROM Game_Question WHERE played = 0 AND gameID = ?
        """, (gameID,))
        rows = self.cursor.fetchall()
        
        if rows:
            ids = [row[0] for row in rows]
            return random.choice(ids)
        return None

    def get_question(self, questionID):
        """
        Holt die Frage und die dazugehörigen Antworten aus der Datenbank.
        """
        self.cursor.execute(""" 
        SELECT question, correct_answer, incorrect_answers1, incorrect_answers2, incorrect_answers3
        FROM Question
        WHERE questionID = ?
        """, (questionID,))
        row = self.cursor.fetchone()  # Verwende fetchone(), da nur eine Frage erwartet wird
        
        if row:
            return {
                "question_text": row[0],
                "correct_answer": row[1],
                "incorrect_answer1": row[2],
                "incorrect_answer2": row[3],
                "incorrect_answer3": row[4]
            }
        return None  # Gibt None zurück, wenn keine Frage gefunden wurde

    def get_correct_answer(self, questionID):
        """
        Holt die korrekte Antwort für eine bestimmte Frage-ID.
        """
        self.cursor.execute(""" 
        SELECT correct_answer FROM Question WHERE questionID = ?
        """, (questionID,))
        row = self.cursor.fetchone()
        
        return row[0] if row else None

    def create_question(self, question, categoryID, difficultyID, correct_answer, incorrect_answer1, incorrect_answer2, incorrect_answer3):
        """
        Erstellt eine neue Frage in der Datenbank.
        """
        self.cursor.execute(""" 
        INSERT INTO Question(question, categoryID, difficultyID, correct_answer, incorrect_answers1, incorrect_answers2, incorrect_answers3) 
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (question, categoryID, difficultyID, correct_answer, incorrect_answer1, incorrect_answer2, incorrect_answer3))
        self.con.commit()   
        
        return "Question created! :)"
    
    def update_question(self, questionID, input_field, user_change):
        """
        Aktualisiert ein bestimmtes Feld einer Frage in der Datenbank.
        """
        self.cursor.execute(f""" UPDATE Question SET {input_field} = ? WHERE questionID = ? """, (user_change, questionID))
        self.con.commit()  
        return f"Question {questionID} was changed"
         
    def delete_question(self, questionID):
        """
        Löscht eine Frage aus der Datenbank.
        """
        self.cursor.execute("""DELETE FROM Question WHERE questionID = ?""", (questionID,))
        self.con.commit() 
    
    def fill_right_or_wrong(self, playerID, gameID, questionID, right):
        """
        Füllt die Tabelle right_or_wrong mit den Spielerantworten.
        """
        self.cursor.execute("""
                                INSERT INTO right_or_wrong(playerID,gameID,questionID,answerCorrectly) VALUES(?,?,?,?)
                             """, (playerID, gameID, questionID, right))
        self.con.commit()  
        return
    
    def get_question_points(self, questionId):
        """
        Holt die Punkte für eine bestimmte Frage basierend auf der Schwierigkeit.
        """
        self.cursor.execute(""" 
        SELECT d.difficultyID, d.points
        FROM Difficulty d
        JOIN Question q ON d.difficultyID = q.difficultyID
        WHERE q.questionID = ?
        """, (questionId,))
        
        rows = self.cursor.fetchall()
        return [row[0] for row in rows]


