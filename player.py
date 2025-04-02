import sqlite3
con = sqlite3.connect("./Database/database.db")
cursor = con.cursor()

class Player: 

    def __init__(self, name: str, player_id: int, player_password, wins, score,correctHardQuestions,correctMediumQuestions, correctEasyQuestions):
        self.name = name
        self.player_id = player_id
        self.password = player_password
        self.score = score
        self.wins = wins
        self.correctHardQuestions = correctHardQuestions
        self.correctMediumQuestions = correctMediumQuestions
        self.correctEasyQuestions = correctEasyQuestions

    def add_score (self, punkte: int):
        self.score = punkte
        return

    def get_score (self):
        return self.score
        
    def get_winns(self):
        return self.wins
        
    def get_games(self):
        return
        
    def get_answer(self):
        return
        
    def insert_answer(self):
        return
        
        
    def get_playerID(self):
        cursor.execute(""" 
            SELECT playerID FROM Player Where Name = ?""", (self.name,))
        return cursor.fetchall()

    def create_user(self):
        return
        
    def receive_achievement(self, achievement_requirements, achievementID, player_achievements):
        requirement, required_value = achievement_requirements

        # Sicherstellen, dass player_achievements eine Liste oder ein Tupel ist
        if not isinstance(player_achievements, (list, tuple)):
            player_achievements = [player_achievements]
        
        # Prüfen, ob player_achievements leer ist
        if not player_achievements:
            return  # Falls player_achievements leer ist, sofort zurückkehren
        
        # Konvertiere die Liste von Tupeln in eine Liste von Zahlen (Achievement IDs)
        achievement_ids = {ach[0] for ach in player_achievements}  # Set für schnellere Suche

        # Falls Achievement bereits vorhanden ist, abbrechen
        if achievementID in achievement_ids:
            return 

        # Überprüfen, ob das erforderliche Attribut existiert und den Wert erreicht
        current_value = getattr(self, requirement, None)
        if current_value is not None and current_value >= required_value:
            print("Achievement wird vergeben")
            return True, achievementID
