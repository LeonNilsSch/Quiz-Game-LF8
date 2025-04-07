import sqlite3


class DatabaseHelper:
    def __init__(self, db="src/Database/database.db", connection=None):
        if connection:
            self.con = connection
            self.cursor = self.con.cursor()
        else:
            self.db_path = db
            self.con = sqlite3.connect(self.db_path)
            self.cursor = self.con.cursor()

    def get_value_from_table(self, table, column, condition_column, condition_value):

        self.cursor.execute(
            f""" 
        SELECT {column} FROM {table} WHERE {condition_column} = ? 
        """,
            (condition_value,),
        )
        result = self.cursor.fetchall()

        if result:
            # Falls nur eine Zeile mit einem Wert zurückgegeben wurde
            if len(result) == 1 and len(result[0]) == 1:
                return result[0][0]  # Gibt den einzelnen Wert zurück

            # Falls mehrere Zeilen zurückgegeben wurden, aber nur ein Tupel gewünscht ist
            return tuple(result[0]) if len(result) == 1 else tuple(result)

        return None  # Falls kein Wert gefunden wurde

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
