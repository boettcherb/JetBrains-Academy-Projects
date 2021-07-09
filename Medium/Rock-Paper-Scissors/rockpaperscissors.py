import random


def get_options():
    wins = {"rock": "paper", "paper": "scissors", "scissors": "rock"}
    options = input()
    if options != "":
        options = options.split(",")
        for i, option in enumerate(options):
            new_order = options[i + 1:] + options[:i]
            wins[option] = new_order[:len(new_order) // 2]
    return wins


def get_input(choices):
    while True:
        choice = input()
        if choice == "!exit" or choice == "!rating" or choice in choices:
            return choice
        print("Invalid input")


rating = 0
name = input("Enter your name: ")
print(f"Hello, {name}")
with open("rating.txt", "r") as file:
    for line in file:
        line_data = line.split()
        if line_data[0] == name:
            rating = int(line_data[1])
            break
better_than = get_options()
print("Okay, let's start")
while True:
    computer_choice = random.choice(list(better_than.keys()))
    player_choice = get_input(better_than.keys())
    if player_choice == "!exit":
        break
    elif player_choice == "!rating":
        print(f"Your rating: {rating}")
    elif player_choice in better_than[computer_choice]:
        print(f"Well done. The computer chose {computer_choice} and failed")
        rating += 100
    elif computer_choice in better_than[player_choice]:
        print(f"Sorry, but the computer chose {computer_choice}")
    else:
        print(f"There is a draw ({player_choice})")
        rating += 50
print("Bye!")
