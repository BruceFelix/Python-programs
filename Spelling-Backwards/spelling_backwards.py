# function to reverse a string and spell it backwards
def spell(txt):
     """ This function takes in a string and reverses it to be spelled backwards.
     I used slicing to reverse the characters."""
     
     #slicing the string and reversing
    txt = txt[::-1]
    print(txt)
    
#user input
txt = input()

#prints the output
spell(txt)
