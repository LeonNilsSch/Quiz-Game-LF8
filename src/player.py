import sqlite3

con = sqlite3.connect("src/Database/database.db")
cursor = con.cursor()


class Player:

    def __init__(
        self,
        name: str,
        player_id: int,
        player_password,
        wins,
        score,
        correctHardQuestions,
        correctMediumQuestions,
        correctEasyQuestions,
    ):
        self.name = name
        self.player_id = player_id
        self.password = player_password
        self.score = score
        self.wins = wins
        self.correctHardQuestions = correctHardQuestions
        self.correctMediumQuestions = correctMediumQuestions
        self.correctEasyQuestions = correctEasyQuestions


    def receive_achievement(
    self, achievement_requirements, achievementID, player_achievements
):
        requirement, required_value = achievement_requirements

        # Wenn player_achievements None ist oder ein einzelner int-Wert, umwandeln
        if player_achievements is None:
            player_achievements = []
        elif isinstance(player_achievements, int):
            player_achievements = [(player_achievements,)]  # Ein einzelner int-Wert als Tuple in Liste umwandeln
        elif isinstance(player_achievements, (list, tuple)):
            # Falls es sich um eine Liste/Tupel handelt, aber keine Tupel, dann in (int,) umwandeln
            player_achievements = [(ach,) if isinstance(ach, int) else ach for ach in player_achievements]

        # Nur gültige Einträge extrahieren
        achievement_ids = {ach[0] for ach in player_achievements if isinstance(ach, (tuple, list)) and len(ach) > 0}

        # Falls Achievement bereits vorhanden ist, abbrechen
        if achievementID in achievement_ids:
            return

        # Überprüfen, ob das erforderliche Attribut existiert und den Wert erreicht
        current_value = getattr(self, requirement, None)
        if current_value is not None and current_value >= required_value:
            print("Achievement wird vergeben")
            return True, achievementID

        return False

