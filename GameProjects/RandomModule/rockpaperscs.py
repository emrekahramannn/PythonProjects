# IMPORTS 
from random import choice
from time import sleep


# ITEMS 
ITEMS = ["rock", "paper", "scissors"]


# set game scores
__computer_score = 0
__user_score = 0


# SET THE SCREEN 
CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

def setScreen():
    """
    This function clears the screen and
    move the cursor to the top left when
    called.
    """ 
    print(CLEAR)
    print(CLEAR_AND_RETURN)


# countdown effect
def countDown():
    sleep(1)
    print(3)    # 3
    sleep(1)
    print(2)    # 2
    sleep(1)
    print(1)    # 1


#greeting
def greetUser():
    """
    This function greets user and gives  
    knowledge about how game works.
    """
    global name
    name = input("Please enter your name: ")
    sleep(2)
    setScreen()

    intro = f"""
                                    Welcome to RPS Game.
    Hi {name.capitalize()}. This is a simple Rock - Paper - Scissors game against a random user. 
    You will be asked to enter your choice of either 'Rock', 'Paper' or 'Scissor'. 

    REMEMBER:
        Rock beats Scissors
            Scissor beats Paper
                Paper beats Rock

        and good luck!!!

    Game starts in 3 seconds when you hit enter!
    """

    print(intro)
    input()
    sleep(3)
    setScreen()


# game
def startGame():
    while True:
    # user's item
        while True:
            user_item = input("1-Rock\n2-Paper\n3-Scissors\nEnter your choice (1,2,3): ").lower()
            if user_item in ["1", "2", "3", "rock", "paper", "scissors"]:
                if user_item == "1" or user_item == "rock": 
                    user_item = "rock"
                elif user_item == "2" or user_item == "paper": 
                    user_item = "paper"
                else: 
                    user_item = "scissors" 
                break
            else:
                print("Please enter valid input!")
                sleep(2)
                setScreen()

        # computer's item
        print("User is making his choice. Please wait...")
        sleep(2)
        setScreen()
        comp_item = choice(ITEMS)

        return user_item, comp_item


# winner
def checkWinner(user_item, comp_item):
    if (user_item == "rock" and comp_item == "scissors") or (user_item == "scissors" and comp_item == "paper") or (user_item == "paper" and comp_item == "rock"):
        print(f"{user_item.capitalize()} beats {comp_item.capitalize()}! You win!")
        global __user_score
        __user_score += 1
        sleep(2)
        setScreen()
    elif (comp_item == "rock" and user_item == "scissors") or (comp_item == "scissors" and user_item == "paper") or (comp_item == "paper" and user_item == "rock"):
        print(f"{comp_item.capitalize()} beats {user_item.capitalize()}! User win!")
        global __computer_score
        __computer_score += 1
        sleep(2)
        setScreen()
    elif user_item == comp_item:
        print("No one beats other! Try again.")
        sleep(2)
        setScreen()




greetUser()
while True:
    user_item, comp_item = startGame()
    countDown()
    sleep(1)
    setScreen()
    checkWinner(user_item, comp_item)

    if __user_score == 3:
        print(f"{name.capitalize()} Won!")
        break
    elif __computer_score == 3:
        print("User Won!")
        break
    else:
        continue