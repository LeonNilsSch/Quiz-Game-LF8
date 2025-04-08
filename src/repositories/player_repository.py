from repositories.database_helper import DatabaseHelper
import sqlite3


class PlayerRepository(DatabaseHelper):
    def __init__(self, connection=None):
        super().__init__(connection=connection)
        self.player_id = None 
        
    # def get_playerID_by_name(self, playerName):
    #     self.player_id = self.get_value_from_table("Player", "playerID", "playerName", playerName)
    #     return self.player_id #brauchen wir hier den Return
    
    # def get_playerName(self,playerName):
    #     test= print(self.get_value_from_table("Player", "playerName", "playerName", playerName))
    #     return test
    
    # def get_player_field_value(self, wanted_Field, search_with_field, sear_with_value):
    #     #outputs the desired values ​​from the "Player" table.
    #     value = self.get_value_from_table("Player", wanted_Field, search_with_field, sear_with_value )
    #     if search_with_field == "playerID":
    #         self.player_id = value
    #     return value
    
    # def get_player_password(self):
    #     return self.get_value_from_table("Player", "playerID", "playerName", self.player_id)
        
    # def get_score(self):
    #     return self.get_value_from_table("Player", "playerScore", "playerID", self.player_id)

    # def get_wins(self):
    #     return self.get_value_from_table("Player", "playerWins", "playerID", self.player_id)

    # def get_playedGames(self):
    #     return self.get_value_from_table("Player","playedGames", "playerID", self.player_id)

    def get_player_achievments(self):
        self.cursor.execute(
            """
                            SELECT pta.achievementID, a.achievementID  
                            FROM PlayerToAchievement pta
                            JOIN Achievement a
                            ON a.achievementID = pta.achievementID
                            WHERE pta.playerID = ?
                            """,
            (self.player_id,),
        )
        rows = self.cursor.fetchall()
        return [row[0] for row in rows]
    def get_all_player_infos_by_name(self, playerName): #gibt es schon einmal, welche wollen wir genau benutzen?
        self.get_value_from_table("Player", "*", "playerName", playerName)
        
    def update_playerField(self,updateField, playerID, newValue):
       self.update_fieldValue("Player", updateField, newValue, playerID, "playerID")
    
    def get_playerID(self, playerName): #gibt es schon einmal, welche wollen wir genau benutzen?
        self.get_value_from_table("Player", "playerID", "playerName", playerName)

    def create_user(self, playerName, playerPassword):
        self.cursor.execute(
            """ INSERT INTO Player(playerName, playerPassword) VALUES (?,?)""",
            (
                playerName,
                playerPassword,
            ),
        )
        self.con.commit()
        return

    def delete_user(self, playerID): # es kann eine beliebe PlayerID ausgewählt werden
        self.cursor.execute("""DELETE FROM Player WHERE playerID = ?""", (playerID,))
        self.con.commit()
        return

    def get_all_player_achievements(self):
        return self.get_value_from_table(
            "PlayerToAchievement", "achievementID", "playerID", self.player_id
        )

    def update_high_score(self,playerID, new_score):
        current_score = self.get_value_from_table("Player", "playerScore", "playerID", self.player_id)
        print(current_score)
        if current_score == None or new_score > current_score:
            self.update_fieldValue("Player", "playerScore", new_score, self.player_id, "playerID")
            print(f"Player {playerID} score updated to {new_score}.")
            
    def update_field(self,playerID, plus_value, field):
        current_score = self.get_value_from_table("Player", field, "playerID", playerID)
        print(current_score)
        if plus_value != None:
            new_value = current_score + plus_value
            self.update_fieldValue("Player", field, new_value, playerID, "playerID")
            print(f"Player {playerID} score updated to {new_value}.")
            

            

    def get_all_players_sorted_by_score(self):
        self.cursor.execute(
            """SELECT playerName, playerScore FROM Player ORDER BY playerScore DESC"""
        )
        rows = self.cursor.fetchall()
        return [{"playerName": row[0], "playerScore": row[1]} for row in rows]
    
    
