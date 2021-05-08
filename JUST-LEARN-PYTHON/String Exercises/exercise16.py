#Given a strings check first and last words are same.
# ex = 'Apples should compare with Apples' 
# if ex.startswith("Apples") and ex.endswith("Apples"):
#     print("same") my version

#Onlines answer

given_string = " Apples should compared with Apples"
 
 
word_list = given_string.strip().split()
 
if word_list[0] == word_list[-1]:
    print("First and last words are same")
     
else:
     
    print("First and last words are not same")