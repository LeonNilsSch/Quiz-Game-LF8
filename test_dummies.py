import sqlite3

con = sqlite3.connect("database.db")
# Cursor-Objekt zum Ausführen von SQL-Befehlen
cursor = con.cursor()

# Beispiel-Tabelle erstellen
cursor.execute("""INSERT INTO Player (playerName, playerScore) VALUES ("Leon", 10) """)
cursor.execute("""INSERT INTO Player (playerName, playerScore) VALUES ("Jana", 100) """)
cursor.execute("""INSERT INTO Player (playerName, playerScore) VALUES ("Luka", 1000) """)
# Änderungen speichern und Verbindung schließen
con.commit()
con.close()