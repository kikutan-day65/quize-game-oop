from question_model import Question
from data import question_data

question_bank = []
for question in question_data:
    question_text = question['text']
    question_anwer = question['answer']
    new_question = Question(question, question_anwer)
    question_bank.append(new_question)
