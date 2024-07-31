class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print(f"You got it right! Your score: {self.score}/{self.question_number + 1}")
        else:
            print(f"That's wrong. Your score: {self.score}/{self.question_number + 1}")
        print("\n")

    def next(self):
        answer = input(f'Q.{self.question_number + 1}: {self.question_list[self.question_number].text} (True/False)?: ')
        self.check_answer(answer, self.question_list[self.question_number].answer)
        self.question_number += 1
