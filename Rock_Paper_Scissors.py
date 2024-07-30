import random as rand

# CODE FOR BEST OF THREE OF ROCK PAPER SCISSORS

user_score = 0
comp_score = 0
event = ''

while True:
    choice = int(input("Choose between Rock, Paper, Scissors\n 0 for Rock, 1 for Paper and 2 for Scissors"))
    options = ["Rock", "Paper", "Scissors"]
    comp_choice = rand.randint(0, 2)
    print(f"Computer's Choice: {options[comp_choice]}")

    if choice > 2 or choice < 0:
        event = "lose"
        print("You typed an invalid number, You lose")
    elif choice == comp_choice:
        event = "draw"
        print("Draw")
    elif choice == 0 and comp_choice == 2:
        event = "win"
    elif comp_choice == 0 and choice == 2:
        event = "lose"
    elif choice > comp_choice:
        event = "win"
    elif comp_choice > choice:
        event = "lose"

    if event == "win":
        user_score = user_score + 1
        print(f"You Won \nYour Score: {user_score}\nComputer's score: {comp_score}")
    elif event == "lose":
        comp_score = comp_score + 1
        print(f"You Lost \nYour Score: {user_score}\nComputer's score: {comp_score}")

    if user_score == 2:
        print("CONGRATULATIONS\nYou won the Best Of Three")
        again = input("Play again: (y,n)")
        if again.lower() != "y":
            break
    elif comp_score == 2:
        print("You lost the Best Of Three")
        again = input("Play again: (y,n)")
        if again.lower() != "y":
            break
