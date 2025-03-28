import datetime
import sqlite3
import uuid
con = sqlite3.connect("database.db")
cursor = con.cursor()

class Game:
    def __init__(self,gameID, winner, questions):
        self.gameID = gameID
        self.winner = winner
        self.questions = questions
        
        
    
    def create_game(self):
        date = datetime.datetime.now()
        game_code = str(uuid.uuid4())[:8]  # Kürzerer Code für das Spiel

        cursor.execute("INSERT INTO Game (name, game_code, date) VALUES (?, ?)", 
               ("Neues Spiel", game_code))
        con.commit()  
        return
    
    def fill_game_table(self):
        cursor.execute(""" 
            INSERT INTO Game(gameID, questionID, played) Values(?,?,0)
            """)
        con.commit()   
        return
        
    def get_answer_of_player(self):
        return
   
    def fill_player_of_game(self):
        return
    