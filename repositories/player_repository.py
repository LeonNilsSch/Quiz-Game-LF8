import sqlite3
from repositories.database_helper import DatabaseHelper
class PlayerRepoisitory(DatabaseHelper):
    def get_playerID_by_name(self, name):
        return self.get_value_from_table("Player", "playerID", "playerName",name)
    
    def get_score (self,playerID):
        return self.get_value_from_table("Player", "playerScore", "playerID", playerID)
        
    
    def update_score (self, newScore, playerID ):
        self.cursor.execute(""" UPDATE Player SET playerScore = ? WHERE playerID = ?""",(newScore,playerID))
        self.con.commit()  
        return 

    def get_winns(self,playerID):
        return self.get_value_from_table("Player", "winns", "playerID", playerID)
    
    def update_winns(self):
        
        return
        
    def get_playedGames(self,playerID):
        
        return
    
    def update_playedGames(self):
        
        return


    def get_player_achievments(self,playerID):
        self.cursor.execute("""
                            SELECT pta.achievementID, a.achievementID  
                            FROM Player_to_achievement pta
                            JOIN Achievement a
                            ON a.achievementID = pta.achievementID
                            WHERE pta.playerID = ?
                            """, (playerID,))
        rows = self.cursor.fetchall()
        return [row[0] for row in rows]
    
    def get_playerID(self, name):
        self.get_value_from_table("Player", "playerID","name", name)

    def create_user(self, player_name, ):
        self.cursor.execute(""" INSERT INTO Player(name) VALUES (?)""",(player_name,))    
        self.con.commit()  
        return
    
    def change_player_name(self):
        return
    
    def change_player_passwort(self):
        return
    
    def get_all_player_achievements(self,playerID):
        return self.get_value_from_table("Player_to_achievement", "achievementID", "playerID", playerID)
    # def get_requierments(self):
    #     self.cursor.execute("""ALTER TABLE Player ADD COLUMN playedGames INTEGER;""")
    #     self.con.commit()
    
    
    