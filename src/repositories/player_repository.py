from repositories.database_helper import DatabaseHelper
import sqlite3
class PlayerRepository(DatabaseHelper):
    def get_playerID_by_name(self, playerName):
        return self.get_value_from_table("Player", "playerID", "playerName",playerName)
    
    def get_score (self,playerID):
        return self.get_value_from_table("Player", "playerScore", "playerID", playerID)
        

    def get_wins(self,playerID):
        return self.get_value_from_table("Player", "playerWins", "playerID", playerID)
    
        
    def get_playedGames(self,playerID):
        self.cursor.execute("""
                            SELECT COUNT(*) FROM GameOfPlayer
                            WHERE playerID = ?
                                    """, (playerID,))

        anzahl_spiele = self.cursor.fetchone()[0]
        return anzahl_spiele     


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
    
    def get_playerID(self, playerName):
        self.get_value_from_table("Player", "playerID","playerName", playerName)

    def create_user(self, playerName, playerPassword):
        self.cursor.execute(""" INSERT INTO Player(playerName, playerPassword) VALUES (?,?)""",(playerName,playerPassword,))    
        self.con.commit()  
        return
    
    def delete_user(self, playerID):
        self.cursor.execute("""DELETE FROM Player WHERE playerID = ?""", (playerID,))
        self.con.commit() 
        return
    
    def get_all_player_achievements(self,playerID):
        return self.get_value_from_table("PlayerToAchievement", "achievementID", "playerID", playerID)
    
    def get_correct_Questions_by_difficulty(self, playerID, difficultyName):
        self.cursor.execute("""SELECT COUNT(*) AS total_correct
                                FROM RightOrWrong rw
                                JOIN Question q ON rw.questionID = q.questionID
                                JOIN Difficulty d ON q.difficultyID = d.difficultyID
                                JOIN Player p ON rw.playerID = p.playerID
                                WHERE rw.answerCorrectly = TRUE
                                AND d.difficultyName = ?
                                AND p.playerID = ?;""", (difficultyName ,playerID,))
        rows = self.cursor.fetchone()
        print(rows[0])
        return rows[0]
    
    # def update_playerField(self,updateField, playerID, newValue):
    #     self.update_fieldValue("Player", updateField, newValue, playerID, "playerID")

    
    