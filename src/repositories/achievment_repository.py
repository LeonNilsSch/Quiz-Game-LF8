from repositories.database_helper import DatabaseHelper


class AchievmentRepository(DatabaseHelper):
    # keine Init, da es keinen Nutzen dafür gibt, da es keine durchgehed gleiche AchievementID hier gibt, sonder diese immer Wechseln kann
    def get_achievment_name(self, achievementID):
        return self.get_value_from_table(
            "Achievement", "achievementName", "achievementID", achievementID
        )

    def fill_player_to_achievments(
        self,
        playerID,
        achievementID,
    ):
        for i in achievementID:
            self.cursor.execute(
                """INSERT INTO PlayerToAchievement(playerID,achievementID) VALUES (?,?) """,
                (playerID, i),
            )
            self.con.commit()
            print("You have achieved a new achievements")

    def create_new_achievments(self, achievementName, conditionType, value):
        self.cursor.execute(
            """INSERT INTO Achievement (achievementName, conditionType, value) VALUES (?, ?,?) """,
            (achievementName, conditionType, value),
        )
        self.con.commit()

    def get_requierments(self, achievementID):
        requierments = self.get_value_from_table(
            "Achievement", "conditionType, value", "achievementID", achievementID
        )

        print(requierments)
        return requierments

    def get_all_achievements(self):
        self.cursor.execute(""" SELECT * FROM Achievement""")
        rows = self.cursor.fetchall()
        return (
            ([row[0] for row in rows]),
            ([row[2] for row in rows]),
            ([row[3] for row in rows]),
        )
