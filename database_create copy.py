import sqlite3
con = sqlite3.connect("database.db")
# Cursor-Objekt zum Ausführen von SQL-Befehlen
cursor = con.cursor()

# Beispiel-Tabelle erstellen
cursor.execute("""
CREATE TABLE IF NOT EXISTS Category (
    categoryID INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Difficulty (
    difficultyID INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    Points INTEGER NOT NULL,
    description TEXT
);
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS Question (
    questionID INTEGER PRIMARY KEY AUTOINCREMENT,
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
CREATE TABLE IF NOT EXISTS Game (
    gameID INTEGER PRIMARY KEY AUTOINCREMENT,
    winnerID NTEGER,
    date DATE,
    FOREIGN KEY (winnerID) REFERENCES Player(playerID)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Player (
    playerID INTEGER PRIMARY KEY AUTOINCREMENT,
    playerName TEXT,
    playerScore INT,
    wins TEXT
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Player_of_Game (
    gameID INTEGER,
    playerID NTEGER,
    FOREIGN KEY (playerID) REFERENCES Player(playerID),
    FOREIGN KEY (gameID) REFERENCES Game(gameID)
);
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS Game_Question (
    gameID INTEGER,
    questionID NTEGER,
    played BOOLEAN
    FOREIGN KEY (questionID) REFERENCES Question(questionID),
    FOREIGN KEY (gameID) REFERENCES Game(gameID)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Achievment (
    achievmentID INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    points INTEGER
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Player_to_achievment (
    playerID INTEGER,
    questionID NTEGER,
    FOREIGN KEY (playerID) REFERENCES Player(playerID),
    FOREIGN KEY (achievmentID) REFERENCES Achievment(achievmentID)
);
""")

# Änderungen speichern und Verbindung schließen
con.commit()
con.close()
