class Question:
    def __init__(self, text, options, correct_answer, category):
        self.text = text
        self.options = options
        self.correct_answer = correct_answer
        self.category = category

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0