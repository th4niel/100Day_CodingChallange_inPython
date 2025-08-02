"""TODO 1: Create class called QuizBrain"""
"""TODO 2: Write an __init__() method"""
"""TODO 3: initialize the question_number to 0"""
"""TODO 4: initialize the question_list to input """
"""TODO 5: Retrieve the item at the current question_number from the question_list """
"""TODO 6: use the input() function to show the user question text and ask the user answer """
"""TODO 7: Create method still_has_question()"""
"""TODO 8: Return a boolean depending  on the value of question_number"""
"""TODO 9: Use the while loop to show the next_question until the end """

class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}:{current_question.text}. (True/False)?: ")
        self.check_answer(user_answer, current_question.answer)

    def still_has_question(self):
        return self.question_number < len(self.question_list)
    
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:       
            print("Your answer is incorrect!")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")