import sqlite3

class DatabaseHelper:
    def __init__(self, db ="Database/database.db"):
        self.con = sqlite3.connect(db)
        self.cursor = self.con.cursor()
    
    
    def get_value_from_table(self, table, column, condition_column, condition_value):
        self.cursor.execute(f""" 
        SELECT {column} FROM {table} WHERE {condition_column} = ? 
        """, (condition_value,))
        result = self.cursor.fetchone()
        
        if result:
            print(result[0])  # Falls Debugging gewünscht ist
            return result[0]
        
        return None  # Falls kein Wert gefunden wurde