# Ask the user for a number, to pick the color from the list.
# Blue, Green, Orange, Red
# and print the color.

colors = """
To choose a color select:
    1 for Blue
    2 for Green
    3 for Orange 
    4 for Red """
print(colors)
choice = input()

if choice == "1":
    print("You choose Blue.")
elif choice == "2":
    print("You choose Green.")
elif choice == "3":
    print("You choose Orange.")
elif choice == "4":
    print("You choose Red.")
else:
    print("Your choice is invalid.")


