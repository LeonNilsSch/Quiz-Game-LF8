from repositories.database_helper import DatabaseHelper


class CatecoryRepository(DatabaseHelper):
    def get_category_id_by_name(self, categoryName):
        return self.get_value_from_table(
            "Category", "categoryID", "categoryName", categoryName
        )

    def create_category(self, categoryName):
        self.cursor.execute(
            """ 
        INSERT INTO Category(catecoryName) VALUES (?)
        """,
            (categoryName,),
        )
