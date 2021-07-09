import random

better = {"rock": "paper", "paper": "scissors", "scissors": "rock"}
computer_choice = random.choice(("rock", "paper", "scissors"))
player_choice = input()
if player_choice == better[computer_choice]:
    print(f"Well done. The computer chose {computer_choice} and failed")
elif computer_choice == better[player_choice]:
    print(f"Sorry, but the computer chose {computer_choice}")
else:
    print(f"There is a draw ({player_choice})")
