# import modules
import random    # -> to chose a random character in a set of characters random.choice
import string    # -> to create the character set using string.ascii_letters, string.digits, and string.punctuation


def generate_password(min_length: int, numbers=True, special_characters=True) -> str:
    """
    This function creates a password according to given parameters.

    param1: min_length (int)
    param2: numbers (bool)
    param3: special_characters (bool)

    generate_password(10, True, True)
    >>> nmk)ejIS`1
    """

    letters = string.ascii_letters # all of the upper and lowercase letters
    digits = string.digits  # all of the numbers between 0-9
    special = string.punctuation  # all of the special characters

    #set the character set to choose from 
    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    # initial conditions
    pwd = ""               # initially we do not have a pwd
    meets_criteria = False # initially we do not meet the criteria
    has_number = False     # initially we do not have numbers in our pwd
    has_special = False    # initially we do not have special characters in our pwd

    # this loop continues until we met the criteria or the desired length
    while not meets_criteria or len(pwd) < min_length:
        # choose a character in the characters set 
        new_char = random.choice(characters)
        # add this character to the pwd
        pwd += new_char

        # update the initial conditions
        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True
        
        # update the loop condition meets_criteria
        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special

    # check for password quality
    if min_length > 12 and numbers and special_characters:
        print("Strong password")
    elif (min_length > 12 and numbers) or (min_length > 12 and special_characters) or (6 < min_length < 12 and special_characters and numbers):
        print("Good password")
    else:
        print("You should choose a better password")
    
    return pwd



if __name__ == "__main__":
    min_length = int(input("Enter the minimum lenght: "))
    has_number = input("Do you want to have numbers (y/n)? ").lower() == "y"
    has_special = input("Do you want to have special characters (y/n)? ").lower() == "y"
    pwd = generate_password(min_length, has_number, has_special)
    print("The generated password is:", pwd)