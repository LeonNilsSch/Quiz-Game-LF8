import sqlite3
from question_repository import QuestionRepository
from question import Question
from game_repository import Game
from category_repository import CatecoryRepository
from difficulty_repository import DifficultyRepository
# Verbindung zur Datenbank herstellen
# con = sqlite3.connect("database.db")
# Frage-Objekt erstellen


# g = Game(ids,"Politics")

# game_code=g.create_game()
# g.fill_player_of_game(game_code)
category_repo = CatecoryRepository()
categoryID = category_repo.get_category_id_by_name("Politics")

q = Question("Sample question", ["Option1", "Option2"], "Option1", "Politics")
rq = QuestionRepository()
#get_questionID über das Objekt (Instanz) der Klasse aufrufen
ids= rq.get_questionIDs_with_Categorys(categoryID)
rq.fill_game_question(ids, 1)
questionid=rq.get_random_questionID(1)
rq.get_question(questionid)
rq.get_correct_answer(questionid)

d = DifficultyRepository()
difficultyid = d.get_difficultyId_from_questionId(questionid)
d.get_difficulty_points(difficultyid)
d.get_all_difficulties()

# Verbindung schließen
# con.commit()
# con.close()


