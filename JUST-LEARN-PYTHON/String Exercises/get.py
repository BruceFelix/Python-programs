# # arr = "10,20,30,40,50,60,70", get "50 , 60"
# arr = "10,20,30,40,50,60,70"
# if ("50"  in arr) and ("60"  in  arr):
#     print("50, 60")

arr = "10,20,30,40,50,60,70" # get "50,60"
 
new_str = ",".join(arr.split(',')[4:6])
 
print(new_str)
 
#using negative index
new_str = ",".join(arr.split(',')[-3:-1])
 
print(new_str)
 