#Decleration of variables
largest = None
smallest = None
num_list =[]
#Logic loop
while True:
    try:
        number = input("Enter a number :")
        if number == "Done" or number == "done":
                print("Loop breaking")
                break
        number = int(number)
        num_list.append(number)
    except ValueError:
        print("invalid input")
        continue
print(num_list)
largest = max(num_list)
smallest = min(num_list)
print( "The largest value in num_list is " + str(largest))
print("The smallest values in num_list is " +str(smallest))
