# Emre Kahraman
# Quiz APP in OOP Way

class Question():

    def __init__(self, text: str, choices: list, answer: str):
        self.text = text
        self.choices = choices
        self.answer = answer

    def checkAnswer(self, answer):
        return self.answer == answer


q1 = Question("What is the best programming language in 2023 ?", ["C#", "Python", "Java", "Javascript"], "Python")
q2 = Question("What is the most popular programming language in 2023 ?", ["Python", "Java", "C#", "Javascript"], "Python")
q3 = Question("What is the most user-friendly programming language ?", ["C#", "Java", "Python", "Javascript"], "Python")
q4 = Question("What is the most loved programming language ?", ["C#", "Python", "Java", "Javascript"], "Python")
q5 = Question("Wnat is the easiest programming language ?", ["C#", "Python", "Java", "Javascript"], "Python")


questions = [q1, q2, q3, q4, q5]