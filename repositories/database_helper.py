import sqlite3

class DatabaseHelper:
    def __init__(self, db ="Database/database.db"):
        self.con = sqlite3.connect(db)
        self.cursor = self.con.cursor()
    
    
    def get_value_from_table(self, table, column, condition_column, condition_value):
        self.cursor.execute(f""" 
        SELECT {column} FROM {table} WHERE {condition_column} = ? 
        """, (condition_value,))
        result = self.cursor.fetchall()
        
        if result:
        # Wenn ein Wert zurückgegeben wurde, aber nur ein Wert erwartet wird
            if len(result[0]) == 1:
                return result[0][0]  # Gibt den Wert ohne Klammern zurück (als Integer oder String)
            
            # Wenn mehrere Werte im Tupel sind, dann tupel entpacken
            else:
                return result[0]  # Gibt das Tupel zurück

        return None  # Falls kein Wert gefunden wurde