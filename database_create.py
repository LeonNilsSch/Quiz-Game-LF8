import sqlite3
con = sqlite3.connect("database.db")
# Cursor-Objekt zum Ausführen von SQL-Befehlen
cursor = con.cursor()

# Beispiel-Tabelle erstellen
cursor.execute("""
CREATE TABLE IF NOT EXISTS Category (
    CategoryID INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Difficulty (
    DifficultyID INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    Points INTEGER NOT NULL,
    description TEXT
);
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS Question (
    QuestionID INTEGER PRIMARY KEY AUTOINCREMENT,
    categoryID INTEGER,
    difficultyID INTEGER,
    question TEXT NOT NULL,
    correct_answer TEXT NOT NULL,
    incorrect_answers1 TEXT,
    incorrect_answers2 TEXT,
    incorrect_answers3 TEXT,
    FOREIGN KEY (categoryID) REFERENCES Category(CategoryID),
    FOREIGN KEY (difficultyID) REFERENCES Difficulty(DifficultyID)
);
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS Player (
    PlayerID INTEGER PRIMARY KEY AUTOINCREMENT,
    playerName TEXT,
    playerScore INT
);
""")

# Änderungen speichern und Verbindung schließen
con.commit()
con.close()
