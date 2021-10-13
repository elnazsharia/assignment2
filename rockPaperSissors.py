
import random
from typing import Counter

user_score = 0
computer_score = 0
counter = 0

while (counter < 6):
    print("Enter choice \n 1. Rock \n 2. paper \n 3. scissor \n")

    choice = int(input("User: "))

    while choice > 3 or choice < 1:
        choice = int(input("enter valid input: "))

    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'paper'
    else:
        choice_name = 'scissor'

    print("user choice is: " + choice_name)
    print("\nNow its computer turn.......")

    comp_choice = random.randint(1, 3)

    while comp_choice == choice:
        comp_choice = random.randint(1, 3)

    if comp_choice == 1:
        comp_choice_name = 'Rock'
    elif comp_choice == 2:
        comp_choice_name = 'paper'
    else:
        comp_choice_name = 'scissor'

    print("Computer choice is: " + comp_choice_name)

    print(choice_name + " V/s " + comp_choice_name)

    # condition for winning
    if(choice == 2):
        if(comp_choice == 1):
            print("paper wins => ")
            result = "paper"
            user_score += 1
        elif(comp_choice == 2):
            print("equal")
        elif(comp_choice == 3):
            print("sissors wins => ")
            result = "sissors"
            computer_score + 1

    elif(choice == 1):
        if(comp_choice == 1):
            print("equal")
        elif(comp_choice == 2):
            print("paper wins => ")
            result = "paper"
            computer_score += 1
        elif(comp_choice == 3):
            print("rock wins => ")
            result = "rock"
            user_score + 1

    if(choice == 3):
        if(comp_choice == 1):
            print("rock wins => ")
            result = "rock"
            computer_score += 1
        elif(comp_choice == 2):
            print("sissors wins =>")
            result = "sissors"
            user_score += 1
        elif(comp_choice == 3):
            print("equal")
    counter += 1

print("Thank you for playing")
print("computer Scores " + str(computer_score))
print("user scores " + str(user_score))

if(computer_score > user_score):
    print("Computer Won the Game")
else:
    print("User Won the Game")
