# This program calculates the bill to be paid at restaurants bars etc
# from line 3 to line 5 takes input from the user 
billTotal = float(input("Enter the total dollar amount "))
percentageTip  = float(input("What percentage tip are you willing to give? "))
peopleSplittingTheBill = float(input("How many people are splitting the bill? "))

#line 8 and line 9 do some calculations
totalBill = (billTotal * percentageTip / 100) + billTotal # calculates the total bill including the tip
amountToBePaidByEachPerson = totalBill/peopleSplittingTheBill #calculates the amount to be paid by each person inclusive the tip
print("Each person should pay: ")
print(amountToBePaidByEachPerson)
"""
Lets say the bill was 400 and you were 4 people so each person = 100 each
"""
