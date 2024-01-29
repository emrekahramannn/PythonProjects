from random import choice
word_list = ["python", "print", "random", "while", "choice"] 
word = choice(word_list)

hangman_pic = ["""
  +-----+
  o     |  
 /|\    |
 / \    |
       _ _ _""", """
  +-----+
  o     |  
 /|\    |
 /      |
       _ _ _""","""
  +-----+
  o     |  
 /|\    |
        |
       _ _ _ """, """
  +-----+
  o     |  
 /|     |
        |
       _ _ _ """, """
  +-----+
  o     |  
  |     |
        |
       _ _ _ """, """
  +-----+
  o     |  
        |
        |
       _ _ _ """, """
  +-----+
        |  
        |
        |
       _ _ _ """
]

correctLetter = []              # keep track of correct input (letter)
wrongLetter = []                # keep track of wrong input (letter)

chance = len(hangman_pic)       # keep track of total attempts

while chance > 0:
    out = ""
    for char in word:
        if char in correctLetter:
            out += char
        else:
            out += "_"

    if out == word:
        break

    print("Word: ", out)            # show _ _ _ _ (word)
    print(hangman_pic[chance-1])    # show HANGMAN
    
    # take input from user
    letter = input()
    # check if letter already written
    if letter in correctLetter or letter in wrongLetter:
        print(letter, "already written!")
    # check if letter in word or not
    elif letter in word:
        print("Correct letter!")
        correctLetter.append(letter)
    else:
        print("Wrong letter!")
        chance -= 1
        wrongLetter.append(letter)


# check if user have any attemmpts
if chance != 0:
    print("Congrats, you win. The word:", word)
else:
    # when all chances are used up and the game is over
    print("Sorry, you lost. The word was:", word)