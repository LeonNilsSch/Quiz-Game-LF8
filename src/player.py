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
    self, achievementIDs, requirements_fields, required_values, player_achievements
):
        achievement_avieved =[]
       # Sicherstellen, dass player_achievements eine Liste von Tupeln ist
        if player_achievements is None:
            player_achievements = []
        elif isinstance(player_achievements, int):
            player_achievements = [(player_achievements,)]
        elif isinstance(player_achievements, (list, tuple)):
            # Jeden Eintrag zu einem Tuple machen, falls nötig
            player_achievements = [
                (ach,) if isinstance(ach, int) else ach
                for ach in player_achievements
            ]

        # Set mit IDs der bereits erhaltenen Achievements
        bereits_erhaltene_ids = {
            eintrag[0] for eintrag in player_achievements
            if isinstance(eintrag, (tuple, list)) and len(eintrag) > 0
        }

        # Durch alle Anforderungen und zugehörigen IDs gehen
        for achievement_id, attribut_name, benoetigter_wert in zip(achievementIDs, requirements_fields, required_values):

            # Prüfen, ob dieses Achievement bereits vorhanden ist
            if achievement_id in bereits_erhaltene_ids:
                continue  # Dann überspringen

            # Den aktuellen Wert des Spielers für das geforderte Attribut holen
            aktueller_wert = getattr(self, attribut_name, None)

            # Wenn Attribut existiert und Wert ausreicht → Achievement vergeben
            if aktueller_wert is not None and aktueller_wert >= benoetigter_wert:
               
                achievement_avieved.append(achievement_id)
                print(f"Achievement {achievement_id} wird vergeben (für {attribut_name} ≥ {benoetigter_wert})")
                
                # Hier könntest du z. B. das Achievement dem Spieler hinzufügen
               # Zum Beispiel: self.add_achievement(achievement_id)
        return achievement_avieved