import sqlite3


class DatabaseHelper:
    def __init__(self, db="Database/database.db", connection=None):
        if connection:
            self.con = connection
            self.cursor = self.con.cursor()
        else:
            self.db_path = db
            self.con = sqlite3.connect(self.db_path)
            self.cursor = self.con.cursor()

    def get_connection(self):
        return self.con

    def get_value_from_table(self, table, column, condition_column, condition_value):
        query = f"SELECT {column} FROM {table} WHERE {condition_column} = ?"
        self.cursor.execute(query, (condition_value,))
        result = self.cursor.fetchone()
        return result[0] if result else None

    def update_fieldValue(self, table, updateField, newValue, id, idField):
        self.cursor.execute(
            f"""UPDATE {table} SET {updateField} = ? WHERE {idField} = ?""",
            (
                newValue,
                id,
            ),
        )
        self.con.commit()
        return print(f"Bei Spieler {id} wurde {updateField} geupdatet")
