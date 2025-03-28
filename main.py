import sqlite3
from question import Question

# Verbindung zur Datenbank herstellen
con = sqlite3.connect("database.db")

# Frage-Objekt erstellen
q = Question("Sample question", ["Option1", "Option2"], "Option1", "Politics")

# get_questionID über das Objekt (Instanz) der Klasse aufrufen
ids = q.get_questionIDs_with_Categorys("Politics")  # Kein `con` und `cursor` mehr nötig, da sie in der Methode selbst erstellt werden
# q.get_question(ids)
q.fill_game_question(ids, 1)
questionid=q.get_random_questionID(1)
q.get_question(1, questionid)
print(q.get_correct_answer(questionid))

# Verbindung schließen
con.commit()
con.close()


