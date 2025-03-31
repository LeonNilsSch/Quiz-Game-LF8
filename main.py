import sqlite3
from repositories.question_repository import QuestionRepository
from question import Question
#from repositories.game_repository import GameRepository
from repositories.category_repository import CatecoryRepository
from repositories.difficulty_repository import DifficultyRepository
from repositories.achievment_repository import AchievmentRepository
from repositories.player_repository import PlayerRepoisitory

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

a =AchievmentRepository()
a.create_new_achievments()

p=PlayerRepoisitory()

# Verbindung schließen
# con.commit()
# con.close()


