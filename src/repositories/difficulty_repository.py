import sqlite3
from repositories.database_helper import DatabaseHelper
class DifficultyRepository(DatabaseHelper):
    def get_difficultyId_from_questionId(self, questionID):
        return self.get_value_from_table("Question", "difficultyID", "questionID", questionID)

    def get_difficulty_points(self, difficultyID):
        return self.get_value_from_table("Difficulty", "points", "difficultyID", difficultyID)

    def get_difficultyid_by_difficultyname(self, name):
        return self.get_value_from_table("Difficulty", "difficultyID", "name", name)
    
    def get_all_difficulties(self):
        self.cursor.execute(""" 
        SELECT * FROM Difficulty
        """)
        difficulties= self.cursor.fetchall()
        print(difficulties)
        return [difficulties[0] for difficulties in difficulties]
    
    
    def update_points(self,new_points,difficultyID):
        self.cursor.execute(""" 
        UPDATE Difficulty SET points = ? WHERE difficultyID = ?
        """, (new_points,difficultyID,))
        self.con.commit()
        