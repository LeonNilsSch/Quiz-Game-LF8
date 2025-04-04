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
    
    # def change_player_name(self):
    #     return
    
    # def change_player_passwort(self):
    #     return
    
    def get_all_player_achievements(self,playerID):
        return self.get_value_from_table("Player_to_achievement", "achievementID", "playerID", playerID)
    
    def get_correct_Questions_by_difficulty(self, playerID, difficulty):
        self.cursor.execute("""SELECT COUNT(*) AS total_correct
                                FROM right_or_wrong rw
                                JOIN Question q ON rw.questionID = q.questionID
                                JOIN Difficulty d ON q.difficultyID = d.difficultyID
                                JOIN Player p ON rw.playerID = p.playerID
                                WHERE rw.answerCorrectly = TRUE
                                AND d.name = ?
                                AND p.playerID = ?;""", (difficulty ,playerID,))
        rows = self.cursor.fetchone()
        print(rows[0])
        return rows[0]
    
    def update_correctDifficultyQuestions(self,update_difficulty, playerID, new_value):
        self.cursor.execute(f"""UPDATE Player SET {update_difficulty} = ? WHERE playerID = ?""",(new_value,playerID,))
        self.con.commit() 
        print(f"Bei Spieler {playerID} wurde {update_difficulty} geupdatet")

    
    