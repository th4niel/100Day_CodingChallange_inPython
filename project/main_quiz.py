import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from data import question_data
from question_model import Question
from quiz_brain import QuizBrain



"""TODO 1: Write for loop to iterate over the question_data"""
"""TODO 2: Create a Question object from each entry  in question_data"""
"""TODO 3: Append each question object to the question_bank"""


question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(q_text=question_text, q_answer=question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()
print("You have completed the quiz !")
print(f"Your final score was: {quiz.score} out of {quiz.question_number}")