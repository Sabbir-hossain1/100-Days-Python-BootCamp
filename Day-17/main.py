# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from question_model import Question
from data import question_data
from quiz_brain import QuizzBrain


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    question_bank = []
    for question in question_data:
        question_text = question["text"]
        question_answer = question["answer"]
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)

    quiz = QuizzBrain(question_bank)
    while quiz.still_has_question():
        quiz.next_question()

    print("You've completed the quiz")
    print(f"Your final score was {quiz.score}/{quiz.question_number}")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
