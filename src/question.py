# gamelogic for question
class Question:
    def __init__(
        self, question_text: str, options: list, correct_answer: str, category: str
    ):
        self.question_text = question_text
        self.options = options
        self.correct_answer = correct_answer
        self.category = category

    def get_next_question(self):
        return

    def calculate_score(self):
        return

    def right_or_wrong(self, answer_player, correct_answer):
        return answer_player == correct_answer
