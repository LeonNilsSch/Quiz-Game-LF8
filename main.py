import sqlite3
from question import Question

# Verbindung zur Datenbank herstellen
con = sqlite3.connect("database.db")

# Frage-Objekt erstellen
q = Question("Sample question", ["Option1", "Option2"], "Option1", "Politics")

# get_questionID über das Objekt (Instanz) der Klasse aufrufen
q.get_questionID()  # Kein `con` und `cursor` mehr nötig, da sie in der Methode selbst erstellt werden

# Verbindung schließen
con.commit()
con.close()