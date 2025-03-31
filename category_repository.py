import sqlite3

class CatecoryRepository:
    def __init__(self, db ="database.db"):
        self.con = sqlite3.connect(db)
        self.cursor = self.con.cursor()
        
    def get_category_id_by_name(self,name):
        self.cursor.execute(""" 
        SELECT categoryID FROM Category WHERE name = ?
        """, (name,))
        row = self.cursor.fetchone()
        print(row[0])
        return row[0]
    
    def create_category(self, name):
        self.cursor.execute(""" 
        INSERT INTO Category(name) VALUES (?)
        """, (name,))