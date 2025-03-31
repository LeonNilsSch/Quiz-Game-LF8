import sqlite3
con = sqlite3.connect("database.db")
cursor = con.cursor()

class Player: 

    def __init__(self, name: str, player_id: int, player_password, wins):
        self.name = name
        self.player_id = player_id
        self.password = player_password
        self.score = 0
        self.wins = 0

        def add_score (self, punkte: int):
            self.score = punkte

        def get_score (self):
            return self.score
        
        def get_winns(self):
            return self.wins
        
        def get_games(self):
            return
        
        def get_answer(self):
            return
        
        def insert_answer(self):
            return
        
        
        def get_playerID(self):
             cursor.execute(""" 
            SELECT playerID FROM Player Where Name = ?""", (self.name,))
             return cursor.fetchall()

        def create_user(self):
            
            return