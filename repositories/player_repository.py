import sqlite3
from repositories.database_helper import DatabaseHelper
class PlayerRepoisitory(DatabaseHelper):
    def get_playerID_by_name(self, name):
        return self.get_value_from_table("Player", "playerID", "playerName",name)
    
    def get_score (self):
        return 
    
    def update_score (self, punkte:int):
        return 

    def get_winns(self,playerID):
        return self.get_value_from_table("Player", "winns", "playerID", playerID)
    
    def update_winns(self):
        return
        
    def get_playedGames(self,playerID):
        return self.get_value_from_table("Player","games")
    
    def update_playedGames(self):
        return

    

    def get_achievments(self):
        return
    
    def get_playerID(self, name):
        self.get_value_from_table("Player", "playerID","name", name)

    def create_user(self, player_name, ):
        self.cursor.execute(""" INSERT INTO Player(name) VALUES (?)""",(player_name,))    
        self.con.commit()  
        return
    
    # def get_requierments(self):
    #     self.cursor.execute("""ALTER TABLE Player ADD COLUMN playedGames INTEGER;""")
    #     self.con.commit()
    
    
    