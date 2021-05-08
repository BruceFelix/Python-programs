#Given two strings check first is reverse of second. Ex 'ABC','CBA'

def is_reverse(s1, s2):
     
    for i in range(len(s)):
         
        if s1[i] != s2[len(s1)-i-1]:
             
            return False
         
    return True
 
s = "ABC"
 
s2 = "CBA"
 
s3 = 'abc'
 
print(is_reverse(s,s2)) #returns True
 
print(is_reverse(s,s3)) #returns False