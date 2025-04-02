import sqlite3
from repositories.question_repository import QuestionRepository
from question import Question
#from repositories.game_repository import GameRepository
from repositories.category_repository import CatecoryRepository
from repositories.difficulty_repository import DifficultyRepository
from repositories.achievment_repository import AchievmentRepository
from repositories.player_repository import PlayerRepoisitory
from player import Player

category_repo = CatecoryRepository()
categoryID = category_repo.get_category_id_by_name("Politics")

q = Question("Sample question", ["Option1", "Option2"], "Option1", "Politics")
rq = QuestionRepository()
ids= rq.get_questionIDs_with_Categorys(categoryID)
rq.fill_game_question(ids, 1)
questionid=rq.get_random_questionID(1)
rq.get_question(questionid)
rq.get_correct_answer(questionid)
print(rq.get_question_points(questionid))

d = DifficultyRepository()
difficultyid = d.get_difficultyId_from_questionId(questionid)
d.get_difficulty_points(difficultyid)
d.get_all_difficulties()

a =AchievmentRepository()
requierments= a.get_requierments(1)
achievementName = a.get_achievment_name(1)
pr=PlayerRepoisitory()
p= Player(player_id=1, name="Leon", player_password=123456, wins=10, score=0, correctHardQuestions = 10, correctMediumQuestions = 5, correctEasyQuestions = 20)
player_achievements = pr.get_all_player_achievements(1)
print(player_achievements)
check_achievment=p.receive_achievement(requierments,2,player_achievements)

if check_achievment:
    a.fill_player_to_achievments(p.player_id,check_achievment[0],check_achievment[1], achievementName)
print(pr.get_player_achievments(1))




