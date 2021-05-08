foosballers = [
    "Mia",
    "Retta",
    "Augustine",
    "Jin",
    "Waylon",
    "Alphonso",
    "Sage",
    "Hubert",
    "Raymon",
    "Monty",
    "Glen",
    "Christi",
    "Patrice",
    "Craig",
    "Dexter",
    "Wally",
    "Ian",
    "Pat"
]

#1 Get the median player
print(foosballers[int(len(foosballers)/2)])

#2 Get the five players in the middle
print(foosballers[7:12])

#3 Add a fake player called "Average player" in the middle
foosballers.insert(int(len(foosballers)/2), "Average player")
# print(foosballers)

#4 Change the "Average player" to uppercase:AVERAGE PLAYER
foosballers[9] = "AVERAGE PLAYER"
# print(foosballers[9])

#5 Add five players 
newFoosBallers = ["Eugene", "Ispen", "Peter", "Jeff", "John"]
foosballers = foosballers + newFoosBallers
# print(foosballers)

#6 Move AVERAGE PLAYER at the center
del foosballers[9]
foosballers[int(len(foosballers)/2)] = "AVERAGE PLAYER"
# print(foosballers)

#7 Five more players but ranked
foosballers.insert(6 ,"Lacy")#lacy is one spot ahead of Hubert
# Though I don't think I excuted it well
foosballers.insert(11,"Rebecca")#Omar is one spot behind Rebecca
foosballers.insert(7,"Otto")#Otto is 8th best in the league
foosballers.insert(-10,"Chauncey") #Chauncey is 10spots from the bottom of the league
print(foosballers)#prints the whole list now

