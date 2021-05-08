password = "Conundrum56$"# default user password

def passwordChecker():
    """
    This function checks to see if the password given by the user matches the one stored in the variable
    """
    userInput = input("Please enter your password: ")
    if userInput == password:#checks if the password is the same as the one stored in the variable
        print("You got it")
    else:
        print("You got it wrong")# if they get it wrong they are informed and the password function is called again until the right answer is given
        passwordChecker()
passwordChecker()