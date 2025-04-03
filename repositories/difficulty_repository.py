import sqlite3
from repositories.database_helper import DatabaseHelper
class DifficultyRepository(DatabaseHelper):
    def get_difficultyId_from_questionId(self, questionID):
        return self.get_value_from_table("Question", "difficultyID", "questionID", questionID)

    def get_difficulty_points(self, difficultyID):
        return self.get_value_from_table("Difficulty", "difficultyPoints", "difficultyID", difficultyID)

    def get_difficultyid_by_name(self, difficultyName):
        return self.get_value_from_table("Difficulty", "difficultyID", "difficultyName", difficultyName)
    
    def get_all_difficulties(self):
        self.cursor.execute(""" 
        SELECT * FROM Difficulty
        """)
        difficulties= self.cursor.fetchall()
        print(difficulties)
        return [difficulties[0] for difficulties in difficulties]
    
    
    def update_points(self,new_points,difficultyID):
        self.cursor.execute(""" 
        UPDATE Difficulty SET difficultyPoints = ? WHERE difficultyID = ?
        """, (new_points,difficultyID,))
        self.con.commit()
        
    def difficulties(self):
        return
    
    def update_difficulties(self):
        return
    
    def delete_difficulties(self, diffficultyID):
        self.cursor.execute(""" DELETE FROM Difficulty WHERE DifficultyID = ?""", (DifficultyID,))
        self.con.commit()
        return
        