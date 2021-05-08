# # # # # # # # # # # # # # # # # # # # # # # # # # # 
#  Program: The collatz sequence
#  Author: Bruce/stack overflow
#  Version: 1.1
#  date: 17th August 2020
#  Description: This program lets the user type in an integer  and keeps calling the collatz() 
#  on that number  until    the function returns the value 1
#  
# # # # # # # # # # # # # # # # # # # # # # # # # # # #


## this is my code
# def collatz(number):
#     """
#     This function calculates the collatz sequence
#     """
#     if number % 2 == 0:
#         print('number // 2 = '+str((number // 2)))
#     else:
#         print('3 * number + 1 = ' +str((3 * number + 1)))

# print('Please input a number')
# num = collatz(int(input()))


### stackoverflows code
def collatz(num):
    """
     This function calculates the collatz sequence and always ends with a one
    """
    while num > 1:
        if num % 2 == 0:
            print(num//2)
            num = num //2
        elif num % 2 ==1:
            print(3*num+1)
            num = 3*num+1
        else:
            print(num)

def getNum():
    global num
    num = (input("> please enter a number "))
    try:
        num = int(num)
    except ValueError:
        print('plese enter a number')
        getNum()
getNum()
collatz(num)
