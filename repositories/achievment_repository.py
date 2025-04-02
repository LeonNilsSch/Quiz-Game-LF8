from repositories.database_helper import DatabaseHelper
class AchievmentRepository(DatabaseHelper):
    def get_achievment_name(self, achievementID):
        return self.get_value_from_table("Achievement","name", "achievementID", achievementID)
    
    def fill_player_to_achievments(self, playerID, achievementID, achieved, achievementName):
        if achieved:
            self.cursor.execute("""INSERT INTO Player_to_achievement(playerID,achievementID) VALUES (?,?) """,(playerID, achievementID))
            self.con.commit()
            print("You have achieved a new achievements. Its "+achievementName+".")
        
    # def get_requierments(self):
    #     self.cursor.execute("""ALTER TABLE Achievement ADD COLUMN requirements TEXT;""")
    #     self.con.commit()
    
    def create_new_achievments(self, name, points, condition_type, value):
        self.cursor.execute("""INSERT INTO Achievement (name, points, condition_type, value) VALUES (?, ?, ?,?) """,(name, points, condition_type,value ))
        self.con.commit() 
        
    def get_requierments(self,achievementID):
        requierments = self.get_value_from_table("Achievement", "condition_type, value", "achievementID", achievementID)
        
        print(requierments)
        return requierments