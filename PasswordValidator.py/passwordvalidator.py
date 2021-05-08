
password = input("Enter your password and it should be 8 characters long: ")# prompts the user to input a password that is atleat  8 characters long

if len(password) < 8:# checks to see if the length of the password is met
    print("Password is too short")
    password = input("Enter password again: ")


confirmPassword = input("Enter your password to confirm ")
if password != confirmPassword :# verifies if the passwords match
    print("Wrong password ")
    confirmPassword = input("Enter password again: ")# if the verfication fails they are prompted again
    if password == confirmPassword:
        print("Password setup successful")
else: 
    print("Password setup successful") # displays a succesful setup