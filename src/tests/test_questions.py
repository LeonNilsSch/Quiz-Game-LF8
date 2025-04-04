import unittest
from question_repository import Questions

class testQuetions(unittest.TestCase):
    def testgetQuestions(self):
        Questions = Questions("hello", [1,2,3,4], "2", "testcat")
        get_questions = Questions.get_question(1,1)
        






if __name__ == '__main__':
    unittest.main()
