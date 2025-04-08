import random
from repositories.database_helper import DatabaseHelper


class QuestionRepository(DatabaseHelper):
    
    def __init__(self, connection=None):
        super().__init__(connection=connection)  # Initialisiert die Verbindung über die Basisklasse
        self.question_id = None
    
    def get_questionIDs_with_Categorys(self, category_id):
        """
        Holt alle Frage-IDs basierend auf der Kategorie-ID.
        """
        self.cursor.execute(
            """
            SELECT questionID
            FROM Question
            WHERE categoryID = ?
            """,
            (category_id,),
        )
        rows = self.cursor.fetchall()
        return [row[0] for row in rows]

    def get_random_questionID(self, questionIDs):
        self.question_id = random.choice(questionIDs)
        return self.question_id
        

    def get_question(self):
        """
        Holt die Frage und die dazugehörigen Antworten aus der Datenbank.
        """
        self.cursor.execute(
            """ 
        SELECT question, correctAnswer, incorrectAnswers1, incorrectAnswers2, incorrectAnswers3, difficultyID
        FROM Question
        WHERE questionID = ?
        """,
            (self.question_id,),
        )
        row = (
            self.cursor.fetchone()
        )  # Verwende fetchone(), da nur eine Frage erwartet wird

        if row:
            return {
                "questionText": row[0],
                "correctAnswer": row[1],
                "incorrectAnswer1": row[2],
                "incorrectAnswer2": row[3],
                "incorrectAnswer3": row[4],
                "difficultyID": row[5]
            }
        return None  # Gibt None zurück, wenn keine Frage gefunden wurde

    def get_correct_answer(self):
        """
        Holt die korrekte Antwort für eine bestimmte Frage-ID.
        """
        self.cursor.execute(
            """ 
        SELECT correctAnswer FROM Question WHERE questionID = ?
        """,
            (self.question_id,),
        )
        row = self.cursor.fetchone()

        return row[0] if row else None

    def create_question(
        self,
        question,
        categoryID,
        difficultyID,
        correctAnswer,
        incorrectAnswer1,
        incorrectAnswer2,
        incorrectAnswer3,
    ):
        """
        Erstellt eine neue Frage in der Datenbank.
        """
        self.cursor.execute(
            """ 
        INSERT INTO Question(question, categoryID, difficultyID, correctAnswer, incorrectAnswers1, incorrectAnswers2, incorrectAnswers3) 
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
            (
                question,
                categoryID,
                difficultyID,
                correctAnswer,
                incorrectAnswer1,
                incorrectAnswer2,
                incorrectAnswer3,
            ),
        )
        self.con.commit()

        return "Question created! :)"
    
    def update_question(self, questionID, inputField, userChange): #hier wird eine beliebe QuestionID übergeben, deswegen kein self.question_id.
        #updatet die ausgwählte frage, mit dem Übergebenden Werten
        self.update_fieldValue(
            "Question", inputField, userChange, questionID, "questionID"
        )

    def delete_question(self, questionID): #hier wird eine beliebe QuestionID übergeben, deswegen kein self.question_id.
        """
        Löscht eine Frage aus der Datenbank.
        """
        self.cursor.execute(
            """DELETE FROM Question WHERE questionID = ?""", (questionID,)
        )
        self.con.commit()


    def get_question_points(self, question_id):
        # Implementation to fetch points for the given question_id
        cursor = self.con.cursor()
        cursor.execute(
            "SELECT difficultyPoints FROM Difficulty WHERE difficultyID = (SELECT difficultyID FROM Question WHERE questionID = ?)",
            (question_id,),
        )
        result = cursor.fetchone()
        return result[0] if result else None


