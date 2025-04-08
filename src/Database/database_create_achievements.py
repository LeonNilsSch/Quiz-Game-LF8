import sqlite3

con = sqlite3.connect("Database/database.db")
# Cursor-Objekt zum Ausführen von SQL-Befehlen
cursor = con.cursor()


# Beispiel-Tabelle erstellen
cursor.execute(
    """INSERT INTO Achievement (achievementName, achievementPoints, conditionType, value) VALUES ("Get 10 hard questions correct",40, "correctHardQuestions", 10) """
)
cursor.execute(
    """INSERT INTO Achievement (achievementName, achievementPoints, conditionType, value) VALUES ("Get 10 medium questions correct",20, "correctMediumQuestions", 10) """
)
cursor.execute(
    """INSERT INTO Achievement (achievementName, achievementPoints, conditionType, value) VALUES ("Get 10 easy questions correct",5, "correctEasyQuestions", 10) """
)
# Änderungen speichern und Verbindung schließen
con.commit()
con.close()
