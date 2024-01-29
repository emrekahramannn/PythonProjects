# import
from random import randint
from time import sleep

# constants
CLEAR = "\033[2J"   # Clear the screen.
CLEAR_AND_RETURN = "\033[H" # Move the cursor to the upper-left corner of the screen.

# greeting function
def greetUser(name): 
    knowledge = """
    This is a simple game where you will be going to guess the number.
    You will decide the range which the number is going to be in and
    then the program will create a random number in this range. After that
    you will guess the number in five times. There will be instructions for
    you to guess the number (less or more). There you go!!!
    The game starts in 3 seconds when you hit enter.
    """

    print(f"Hello, {name.capitalize()}")
    print(f"{knowledge}")
    input()
    sleep(3)


# set the screen
def setScreen():
    print(CLEAR)
    print(CLEAR_AND_RETURN) 


# set range function
def setRange():
    while True:
        lower_range = input("Please choose a lower range for your number: ")
        upper_range = input("Please choose an upper range for your number: ")

        try:
            lower_range, upper_range = int(lower_range), int(upper_range)
        except ValueError:
            print(CLEAR)
            sleep(1)
            print(CLEAR_AND_RETURN)
            print("Inputs must be integer. Please try again")
        else:
            print(f"Your number is going to be in this range: {lower_range} - {upper_range}")
            break
    
    sleep(3)
    return lower_range, upper_range


# GAME 
def game():

    rand_number = randint(r_lower, r_upper)
    gameOver = False
    chances = 0
    while gameOver == False:
    
        guess = input(f"Make your {chances + 1}. guess: ")

        try:
            guess = int(guess)
        except ValueError:
            print("Input must be integer. Please enter a valid input.")
    
        if guess == rand_number:
            print(f"Congratulations! The number was {rand_number}. You guess the number in your {chances + 1} time!")
            break
        elif guess > rand_number:
            print(f"GREATER GUESS!!! Try lower one.")
        else:
            print(f"LOWER GUESS!!! Try greater one.")

        chances += 1

        if chances < 4:
            sleep(2)
            setScreen()
            continue
        elif chances == 4:
            print("Be careful!! This is your last chance.")
        elif chances == 5:
            print(f"The number was {rand_number}!")
            print("GAME OVER!")
            gameOver = True



if __name__ == "__main__":

    # greet user and clear screen
    name = input("Your name: ")
    greetUser(name)
    setScreen()

    # set the range and clear screen
    r_lower, r_upper = setRange()
    setScreen()

    # start the game
    game()