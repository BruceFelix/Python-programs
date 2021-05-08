# letter counter program

#input
letter = input()

#to store key and values
dict = {}


#loop to count repeated letters
for x in letter:
    Key = dict.keys
    if x in key:
        dict[x] += 1
    else:
        dict[x] = 1
#now getting output
print(dict)
