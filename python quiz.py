import requests
from html import unescape
from random import choice

class QUESTION:
  def __init__(self, question, anwser, wrong_anwsers, user_anwser):
    self.question = question
    self.anwser = anwser
    self.wrong_anwsers = wrong_anwsers

def get_int_input(message, error, low, high):
  while True:
    try:
      inpt = int(input(message))
      if low < inpt < high or low == inpt or high == inpt:
        return inpt
      else:
        print(error)
    except ValueError:
      print(error)

response = requests.get("https://opentdb.com/api.php?amount=10&category=28&type=multiple")

data = response.json()['results']

print('''
*********************************************************************
******************** WELCOME TO THE VEHICLE QUIZ ********************
*********************************************************************

''')

questions = [

]
correct_anwsers = [

]
incorrect_anwsers = [

]
print (questions)
print (correct_anwsers)
print (incorrect_anwsers)
for i,question in enumerate(data):
  questions.append(unescape(question["question"]))
  correct_anwsers.append(question["correct_answer"])
  for i,wrong in enumerate(question["incorrect_answers"]):
    incorrect_anwsers.append(wrong)
#while len(questions) >= 1 :
for i in range(len(questions)):
        correct_ans_value = choice(1,4)
        print(questions[i])
        print(correct_ans)