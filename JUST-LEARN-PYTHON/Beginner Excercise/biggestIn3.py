#Take three numbers from user, and print the biggest
num1 = int(input("Enter your first value: "))
num2 = int(input("Enter your second value: "))
num3 = int(input("Enter your last value: "))

if num1 > num2 and num1 > num3:
    print(str(num1)+ " is the biggest.")
elif num2 > num1 and num2 > num3:
    print(str(num2)+ " is the biggest.")

else:
    print(str(num3) + " is the biggest")