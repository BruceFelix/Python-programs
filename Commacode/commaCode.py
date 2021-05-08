# # # # # # # # # # # # # # # # # # # # # # # # # # # #
#  Program: Comma Code
#  Author: Bruce
#  version: 1.1
#  Date: 17th August 2020
#  Description:Takes a list value as an argument and returns a 
#  string with all the items separated by comma and space, and with and inserted before the last item.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

def listTostring(someList):
    a = ''
    for i in range(len(someList)-1):
        a += str(someList[i])
    a += str('and ' + someList[len(someList)-1])
    print (a)

spam = ['apples ', 'bananas ', 'tofu ', ' cats']
listTostring(list)