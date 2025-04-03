import datetime
import sqlite3
import uuid
from repositories.database_helper import DatabaseHelper

class GameRepository(DatabaseHelper):
    def create_game(self):
        date = datetime.datetime.now()
        date_form= date.strftime("%c")
        
        game_code = str(uuid.uuid4())[:8]  # Kürzerer Code für das Spiel

        self.cursor.execute("INSERT INTO Game (gameDate, gameKey) VALUES (?, ?)", 
               (date_form, game_code))
        self.con.commit()  
        return game_code
    
    def get_gameID(self,game_code):
        return self.get_value_from_table("Game", "gameID", "gameKey", game_code)
    
    def fill_player_of_game(self,playerID,GameID):
        self.cursor.execute("INSERT INTO PlayerOfGame (playerID, gameID) VALUES (?, ?)", 
               (playerID, GameID))
        self.con.commit()
        
    def get_player_score_ingame(self):
        return
    
    def update_game_winner(self):
        return
    
        
    
   
    