from repositories.database_helper import DatabaseHelper
class AchievmentRepository(DatabaseHelper):
    def get_achievment_name(self, achievementID):
        return self.get_value_from_table("Achievement","achievementName", "achievementID", achievementID)
    
    def fill_player_to_achievments(self, playerID, achievementID, achieved, achievementName):
        if achieved:
            self.cursor.execute("""INSERT INTO PlayerToAchievement(playerID,achievementID) VALUES (?,?) """,(playerID, achievementID))
            self.con.commit()
            print("You have achieved a new achievements. Its "+achievementName+".")
        
    # def get_requierments(self):
    #     self.cursor.execute("""ALTER TABLE Achievement ADD COLUMN requirements TEXT;""")
    #     self.con.commit()
    
    def create_new_achievments(self, achievementName, points, conditionType, value):
        self.cursor.execute("""INSERT INTO Achievement (achievementName, achievementPoints, conditionType, value) VALUES (?, ?, ?,?) """,(achievementName, points, conditionType,value ))
        self.con.commit() 
        
    def get_requierments(self,achievementID):
        requierments = self.get_value_from_table("Achievement", "conditionType, value", "achievementID", achievementID)
        
        print(requierments)
        return requierments