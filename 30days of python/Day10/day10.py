#level 1
# 1 iterating from 0 to 10
count = 0
while count < 11:
    print(count)
    count +=1
    
#2 Iterating from 10 to 0 counting downwards
number = 10
while number > 0:
    print(number)
    number -= 1

#3 creating a right angled triangle
for i in range(8):# counts the number of rows
    for j in range(i): # uses the value of i to generate the hashes
        print("#", end='')# ends the hashes with spaces instead of newlines
    print()#breaks the line to a new line

#4 creating a rectangle using for loop
for i in range(0,8):
    for j in range(0,8):
        print("#",end='')
    print()