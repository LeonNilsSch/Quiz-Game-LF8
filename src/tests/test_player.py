import unittest
import sqlite3
from repositories.player_repository import PlayerRepository

class TestPlayerRepository(unittest.TestCase):
    def setUp(self):
        """Erstellt eine temporäre In-Memory SQLite-Datenbank für den Test."""
        self.conn = sqlite3.connect(":memory:")  # In-Memory-DB
        self.cursor = self.conn.cursor()

        # Tabelle manuell erstellen
        self.cursor.execute("""
                       CREATE TABLE IF NOT EXISTS Player (
                       playerID INTEGER PRIMARY KEY AUTOINCREMENT,
                       playerPassword TEXT,
                       playerName TEXT UNIQUE,
                       playerScore INTEGER,
                       playerWins TEXT,
                       playedGames INTEGER,
                       correctHardQuestions INTEGER,
                       correctMediumQuestions INTEGER,
                       correctEasyQuestions INTEGER
                       );       
                    """)
        self.conn.commit()

        # Repository nutzt jetzt die in-memory DB über die Verbindung
        self.player = PlayerRepository(connection=self.conn)



    def test_create_Player(self):
        #given
        playerName = "Marsl"
        playerPass = "123456"

        #when
        # Fügt den Player in die Datenbank und guckt ob es erfolgreich war
        self.player.create_user(playerName, playerPass)
        self.cursor.execute("SELECT playerName FROM Player WHERE playerName = ? AND playerPassword = ?", (playerName,playerPass))
        result = self.cursor.fetchone()
        #then
        self.assertIsNotNone(result)  # Prüfen, ob der Player existiert
        self.assertEqual(result[0], playerName,playerPass)        


    def test_update_playerField(self):
        #given
        playerID = 1
        playerName = "Marsl"
        newValue = "Leon"

        #when
        self.player.update_fieldValue("Player",playerName, playerID, newValue,"playerID")
        
        self.cursor.execute("""SELECT playerName FROM Player WHERE playerName = ?""",(newValue,))
        result = self.cursor.fetchone()

        #then
        self.assertIsNotNone(result)
        self.assertEquel(result, newValue)

    def test_delete_user(self):
        #given
        playerID = 1
        playerName = "Leon"

        self.player.delete_user(playerID)
        self.assertIsNone(self.player.get_playerID(playerName))
        
    def tearDown(self):
        """Schließt die Verbindung nach jedem Test."""
        self.conn.close()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestPlayerRepository("test_create_Player"))
    suite.addTest(TestPlayerRepository("test_update_playerField"))
    suite.addTest(TestPlayerRepository("test_delete_User"))
    
    runner = unittest.TextTestRunner()
    runner.run(suite)