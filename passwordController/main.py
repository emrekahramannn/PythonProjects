# import module
import re

def checkPassword(psw:str) -> str:
    """
    This function checks if the given arg is a valid password
    """
    if not re.search("[0-9]", psw):
        print("Password must contain at least one number.")
    elif not re.search("[a-z]", psw):
        print("Password must contain at least one lower case letter.")
    elif not re.search("[A-Z]", psw):
        print("Password must contain at least one upper case letter.")
    elif re.search("\s", psw):
        print("Password can not contain space.")
    else:
        print("Successfull!")
        quit()


count = 0
print("Create a valid password.")
while count < 5:
    psw = input("Password: ")
    checkPassword(psw)



# Alternative
def checkPassword():
    """
        This function make user to enter a valid password
    """
    while True:
            psw = input("Password: ")
            if not re.search("[0-9]", psw):
                print("Password must contain at least one number.")
                continue
            elif not re.search("[a-z]", psw):
                print("Password must contain at least one lower case letter.")
                continue
            elif not re.search("[A-Z]", psw):
                print("Password must contain at least one upper case letter.")
                continue
            elif re.search("\s", psw):
                print("Password can not contain space.")
                continue
            else:
                print("Successfull!")
                break