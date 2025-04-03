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

    def get_wins(self,playerID):
        return self.get_value_from_table("Player", "playerWins", "playerID", playerID)
    
    def update_wins(self,old_wins,playerID):
        newWins = old_wins + 1
        self.cursor.execute(""" UPDATE Player SET playerWins = ? WHERE playerID = ?""",(newWins,playerID))
        self.con.commit()
        return
        
    def get_playedGames(self,playerID):
        
        return
    
    def update_playedGames(self):
        
        return


    def get_player_achievments(self,playerID):
        self.cursor.execute("""
                            SELECT pta.achievementID, a.achievementID  
                            FROM PlayerToAchievement pta
                            JOIN Achievement a
                            ON a.achievementID = pta.achievementID
                            WHERE pta.playerID = ?
                            """, (playerID,))
        rows = self.cursor.fetchall()
        return [row[0] for row in rows]
    
    def get_playerID(self, name):
        self.get_value_from_table("Player", "playerID","playerName", name)

    def create_user(self, player_name, ):
        self.cursor.execute(""" INSERT INTO Player(playerName) VALUES (?)""",(player_name,))    
        self.con.commit()  
        return
    
    def change_player_name(self):
        return
    
    def change_player_passwort(self):
        return
    
    def get_all_player_achievements(self,playerID):
        return self.get_value_from_table("PlayerToAchievement", "achievementID", "playerID", playerID)
    # def get_requierments(self):
    #     self.cursor.execute("""ALTER TABLE Player ADD COLUMN playedGames INTEGER;""")
    #     self.con.commit()
    
    
    