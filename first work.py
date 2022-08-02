name = input ("Type your nane")
print("Welcome", name, "to this adventure!" )

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go?").lower()

if answer == "left":
    answer = input ("You come to a river, you can walk around ot or swim it across? Type walk to walk aroun ")

    if answer == "swim":
        print("You swam across and were eaten by an alligator.")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and lost the game.")
    else:
        print("Not a valid option. You lose.")

elif answer == "right":
    print()
else:
    print("Not a valid option.You lose")

