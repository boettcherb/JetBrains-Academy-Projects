import random


def get_input(choices):
    while True:
        user_input = input()
        if user_input == "!exit" or user_input in choices:
            return user_input
        print("Invalid input")
        
        
better = {"rock": "paper", "paper": "scissors", "scissors": "rock"}
while True:
    computer_choice = random.choice(("rock", "paper", "scissors"))
    player_choice = get_input(better.keys())
    if player_choice == "!exit":
        break
    if player_choice == better[computer_choice]:
        print(f"Well done. The computer chose {computer_choice} and failed")
    elif computer_choice == better[player_choice]:
        print(f"Sorry, but the computer chose {computer_choice}")
    else:
        print(f"There is a draw ({player_choice})")
print("Bye!")
