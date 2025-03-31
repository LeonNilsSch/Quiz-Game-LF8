from repositories.database_helper import DatabaseHelper
class AchievmentRepository(DatabaseHelper):
    def get_achievment_name(self, achievmentID):
        return self.get_value_from_table("Achievment","name", "achievmentID", achievmentID)
    
    def fill_player_to_achievments(self, playerID, achievmentID, requierments):
        self.cursor.execute("""INSRT INTO Player_to_achievement(playerID,achievmentID) VALUES (?,?) """,(playerID, achievmentID))
        self.con.commit()  
        
    # def get_requierments(self):
    #     self.cursor.execute("""ALTER TABLE Achievement ADD COLUMN requirements TEXT;""")
    #     self.con.commit()
    
    def create_new_achievments(self, name, points, requierments):
        self.cursor.execute("""INSRT INTO Achivement (name,points,requierments) VALUES (?,?, ?) """,(name, points, requierments ))
        self.con.commit() 
        
    def get_requierments(self,achievementID):
        return self.get_value_from_table("Achievment", "requierments", "achievmentID", achievementID)
    
    