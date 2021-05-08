#This is a list containing lists with in it
questions = [
    [1,2],
    [2,3],
    [3,4],
    [4,5],
    [5,6],
    [6,7],
    [7,8],
    [8,9],
    [9,10]
]
score = 0 #intializing the score

# using this loop to iterate over all the questions lists
for a,b in questions:
    response = int(input("What's the value of " +str(a) + " + " + str(b) + "? "))# prompting the user to answer the question

    if response == (a+b):# check if the answer they gave is correct
        print("You answered correctly")
        score = score + 1# increment their score if they get the correct answer
    else:
        print("You almost got it but maybe next time you will")
        
  # printing the final score
if score >=  ( len(questions))/2:# checking if their score is great than or equal to a half of the 
    print( str(score) + " That's a great score you are really good at maths")
else:
    print(str(score) + " You did well but there is room for improvement persistence is key")
