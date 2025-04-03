import sqlite3

class DatabaseHelper:
    def __init__(self, db="Database/database.db"):
        self.con = sqlite3.connect(db)
        self.cursor = self.con.cursor()

    def get_value_from_table(self, table, column, condition_column, condition_value):
        self.cursor.execute(f""" 
        SELECT {column} FROM {table} WHERE {condition_column} = ? 
        """, (condition_value,))
        result = self.cursor.fetchall()
        
        if result:
            # Falls nur eine Zeile mit einem Wert zurückgegeben wurde
            if len(result) == 1 and len(result[0]) == 1:
                return result[0][0]  # Gibt den einzelnen Wert zurück

            # Falls mehrere Zeilen zurückgegeben wurden, aber nur ein Tupel gewünscht ist
            return tuple(result[0]) if len(result) == 1 else tuple(result)

        return None  # Falls kein Wert gefunden wurde
