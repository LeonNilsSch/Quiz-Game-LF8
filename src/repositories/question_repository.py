import sqlite3
import random
from repositories.database_helper import DatabaseHelper
class QuestionRepository(DatabaseHelper):
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
        Füllt die Tabelle GameQuestion mit den Frage-IDs für ein bestimmtes Spiel.
        """
        for i in questionids:
            self.cursor.execute(""" 
            INSERT INTO GameQuestion(gameID, questionID, played) VALUES (?, ?, 0)
            """, (gameid, i,))
        self.con.commit()   

    def get_random_questionID(self, gameID):
        """
        Holt eine zufällige Frage-ID aus der Tabelle GameQuestion, die noch nicht gespielt wurde.
        """
        self.cursor.execute(""" 
        SELECT questionID FROM GameQuestion WHERE played = 0 AND gameID = ?
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
        SELECT question, correctAnswer, incorrectAnswers1, incorrectAnswers2, incorrectAnswers3
        FROM Question
        WHERE questionID = ?
        """, (questionID,))
        row = self.cursor.fetchone()  # Verwende fetchone(), da nur eine Frage erwartet wird
        
        if row:
            return {
                "questionText": row[0],
                "correctAnswer": row[1],
                "incorrectAnswer1": row[2],
                "incorrectAnswer2": row[3],
                "incorrectAnswer3": row[4]
            }
        return None  # Gibt None zurück, wenn keine Frage gefunden wurde

    def get_correct_answer(self, questionID):
        """
        Holt die korrekte Antwort für eine bestimmte Frage-ID.
        """
        self.cursor.execute(""" 
        SELECT correctAnswer FROM Question WHERE questionID = ?
        """, (questionID,))
        row = self.cursor.fetchone()
        
        return row[0] if row else None

    def create_question(self, question, categoryID, difficultyID, correctAnswer, incorrectAnswer1, incorrectAnswer2, incorrectAnswer3):
        """
        Erstellt eine neue Frage in der Datenbank.
        """
        self.cursor.execute(""" 
        INSERT INTO Question(question, categoryID, difficultyID, correctAnswer, incorrectAnswers1, incorrectAnswers2, incorrectAnswers3) 
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (question, categoryID, difficultyID, correctAnswer, incorrectAnswer1, incorrectAnswer2, incorrectAnswer3))
        self.con.commit()   
        
        return "Question created! :)"
    
    def update_question(self, questionID, inputField, userChange):
        self.update_fieldValue("Question", inputField, userChange, questionID, "questionID")
         
    def delete_question(self, questionID):
        """
        Löscht eine Frage aus der Datenbank.
        """
        self.cursor.execute("""DELETE FROM Question WHERE questionID = ?""", (questionID,))
        self.con.commit() 
    
    def fill_right_or_wrong(self, playerID, gameID, questionID, right):
        """
        Füllt die Tabelle RightOrWrong mit den Spielerantworten.
        """
        self.cursor.execute("""
                                INSERT INTO RightOrWrong(playerID,gameID,questionID,answerCorrectly) VALUES(?,?,?,?)
                             """, (playerID, gameID, questionID, right))
        self.con.commit()  
        return
    
    def get_question_points(self, questionId):
        """
        Holt die Punkte für eine bestimmte Frage basierend auf der Schwierigkeit.
        """
        self.cursor.execute(""" 
        SELECT d.difficultyID, d.difficultyPoints
        FROM Difficulty d
        JOIN Question q ON d.difficultyID = q.difficultyID
        WHERE q.questionID = ?
        """, (questionId,))
        
        rows = self.cursor.fetchone()
        return rows


