from questions import *

class Quiz():

    def __init__(self, questions: list):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0 

    def getQuestion(self):
        return self.questions[self.questionIndex]
    
    def displayQuuestion(self):
        question = self.getQuestion()
        print(f"Question {self.questionIndex + 1}: {question.text}")

        for choice in question.choices:
            print("-" + choice)

        answer = input("Answer: ")
        self.guess(answer.capitalize())
        self.loadQuestion()


    def guess(self, answer):
        question = self.getQuestion()
        if question.checkAnswer(answer):
            self.score += 1
        self.questionIndex += 1

        
    def loadQuestion(self):
        if len(self.questions) == self.questionIndex:
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuuestion()


    def showScore(self):
        print("Score: ", self.score)

    
    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber = self.questionIndex + 1

        if questionNumber > totalQuestion:
            print("Quiz Done")
        else:
            print(f"Question {questionNumber} of {totalQuestion}".center(100, "*"))



quiz = Quiz(questions)

quiz.loadQuestion()