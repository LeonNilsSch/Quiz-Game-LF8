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
    points INTEGER NOT NULL,
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
    FOREIGN KEY (categoryID) REFERENCES Category(categoryID),
    FOREIGN KEY (difficultyID) REFERENCES Difficulty(difficultyID)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Player (
    playerID INTEGER PRIMARY KEY AUTOINCREMENT,
    playerPassword TEXT,
    playerName TEXT,
    playerScore INTEGER,
    wins TEXT,
    playedGames INTEGER
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Game (
    gameID INTEGER PRIMARY KEY AUTOINCREMENT,
    winnerID INTEGER,
    date DATE,
    game_key TEXT,
    FOREIGN KEY (winnerID) REFERENCES Player(playerID)
    
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Player_of_Game (
    gameID INTEGER,
    playerID INTEGER,
    FOREIGN KEY (playerID) REFERENCES Player(playerID),
    FOREIGN KEY (gameID) REFERENCES Game(gameID)
);
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS Game_Question (
    gameID INTEGER,
    questionID INTEGER,
    played INTEGER,
    FOREIGN KEY (questionID) REFERENCES Question(questionID),
    FOREIGN KEY (gameID) REFERENCES Game(gameID)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Achievement (
    achievementID INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    points INTEGER,
    requirements TEXT
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Player_to_achievement (
    playerID INTEGER,
    achievementID INTEGER,
    FOREIGN KEY (playerID) REFERENCES Player(playerID),
    FOREIGN KEY (achievementID) REFERENCES Achievement(achievementID)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS right_or_wrong (
    playerID INTEGER,
    questionID INTEGER,
    gameID INTEGER,
    answerCorrectly INTEGER,
    FOREIGN KEY (playerID) REFERENCES Player(playerID),
    FOREIGN KEY (questionID) REFERENCES Question(questionID),
    FOREIGN KEY (gameID) REFERENCES Game(gameID)
);
""")

# Änderungen speichern und Verbindung schließen
con.commit()
con.close()
