import sqlite3
import random
con = sqlite3.connect("database.db")
cursor = con.cursor()
        
class Question:
    def __init__(self, question_text: str, options: list, correct_answer: str, category: str):
        self.question_text = question_text
        self.options = options
        self.correct_answer = correct_answer
        self.category = category

    def get_questionID(self):
        selected = []
        # SQL-Abfrage
        cursor.execute(""" 
        SELECT 
            q.QuestionID
        FROM 
            Question q
        JOIN 
            Category c ON q.CategoryID = c.CategoryID
        WHERE
            c.name = "Politics"
        """)
        
        # Ergebnisse holen und ausgeben
        rows = cursor.fetchall()
        # selected.append(rows)

        print(rows)
        
        ids = [rows[0] for rows in rows]
        return ids
    
    
    def get_question(self, ids):
        
        random_choice = random.choice(ids)
        print(random_choice)
        
        cursor.execute(""" 
        SELECT QuestionID, question, correct_answer, incorrect_answers3, incorrect_answers2, incorrect_answers3 FROM Question WHERE QuestionID = ?""",(random_choice,)), 
        rows = cursor.fetchall()
        
        print(rows)
        question = rows[0][1]
        correct_answer = rows[0][2]
        inccorrect_answer1 = rows[0][3]
        inccorrect_answer2 = rows[0][4]
        inccorrect_answer3 = rows[0][5]
        print(question, correct_answer,inccorrect_answer1, inccorrect_answer2,inccorrect_answer3)