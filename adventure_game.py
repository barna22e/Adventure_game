name = input("Type your name: ")
print("Welcome", name, "to this adventure!")
answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim accross? Type to walk walk around and swim to swim accross: ").lower()

    if answer == "swim":
        print("You swam accross and were eaten by an alligator. ")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game 👎")
    else:
        print("Not a valid option. You lose 👎")


elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly, do you want to cross it or head back(cross/back)? ").lower()

    if answer == "back":
        print("You go back to the main road and lose 👎")
    elif answer == "cross":
        answer =input("Cross the bridge and meet a stranger. Do you talk to him (yes/no)? ").lower()

        if answer == "yes":
            answer = input("You will find a way to the castle. But there is a monster on the way. will you go (yes/no)? ").lower()
            if answer == "yes":
                print("You will find treasure. And you WIN!! 🎉🎉 ")
            elif answer == "no":
                print("You ignore the stranger and he kill you. you lose! 👎")
            else:
                print("Not a valid option. You lose 👎")

        elif answer == "no":
            print("You ignore the stranger and he kill you. you lose! 👎")
        else:
            print("Not a valid option. You lose 👎")

    else:
        print("Not a valid option. You lose 👎")

else:
    print("Not a valid option. You lose 👎 ")
print("Thank you for trying", name, "❤️")