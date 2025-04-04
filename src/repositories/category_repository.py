import sqlite3
from repositories.database_helper import DatabaseHelper
class CatecoryRepository(DatabaseHelper):
    def get_category_id_by_name(self,name):
        return self.get_value_from_table("Category", "categoryID", "name", name)
    
    def create_category(self, name):
        self.cursor.execute(""" 
        INSERT INTO Category(name) VALUES (?)
        """, (name,))