import datetime
import sqlite3
import uuid
con = sqlite3.connect("database.db")
cursor = con.cursor()

class Game:
    def __init__(self, questions, category):
        self.questions = questions
        self.category = category
        
    
    def create_game(self):
        date = datetime.datetime.now()
        date_form= date.strftime("%c")
        
        game_code = str(uuid.uuid4())[:8]  # Kürzerer Code für das Spiel

        cursor.execute("INSERT INTO Game (date, game_code) VALUES (?, ?)", 
               (date_form, game_code))
        con.commit()  
        return game_code
    
    def get_gameID(self,game_code):
        cursor.execute("""SELECT gameID FROM Game WHERE game_code = ?""",(game_code,))
        row= cursor.fetchone()
        print(row)
        
        
    
   
    