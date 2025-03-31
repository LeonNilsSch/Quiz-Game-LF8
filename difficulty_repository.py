import sqlite3

class DifficultyRepository:
    def __init__(self, db ="database.db"):
        self.con = sqlite3.connect(db)
        self.cursor = self.con.cursor()
    
    def get_difficultyId_from_questionId(self,questionID):
        self.cursor.execute(""" 
        SELECT difficultyID FROM Question WHERE questionID = ? 
        """, (questionID,))
        id = self.cursor.fetchone()
        print(id[0])
        return id[0]
    
    def get_difficulty_points(self, difficultyID):
        self.cursor.execute(""" 
        SELECT points FROM Difficulty WHERE difficultyID = ? 
        """, (difficultyID,))
        id = self.cursor.fetchone()
        print(id[0])
        return id[0]
    
    def get_all_difficulties(self):
        self.cursor.execute(""" 
        SELECT * FROM Difficulty
        """)
        difficulties= self.cursor.fetchall()
        print(difficulties)
        return [difficulties[0] for difficulties in difficulties]
    
    def get_difficultyid_by_difficultyname(self, name):
        self.cursor.execute(""" 
        SELECT difficultyID FROM Difficulty WHERE name = ? 
        """, (name,))
        id = self.cursor.fetchone()
        print(id[0])
        return id[0]
    
    def update_points(self,new_points,difficultyID):
        self.cursor.execute(""" 
        UPDATE Difficulty SET points = ? WHERE difficultyID = ?
        """, (new_points,difficultyID,))
        self.con.commit()
        