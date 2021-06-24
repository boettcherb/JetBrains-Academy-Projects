import random

print("H A N G M A N")
choice = random.choice(("python", "java", "kotlin", "javascript"))
partial_string = choice[:3] + ((len(choice) - 3) * "-")
if input(f"Guess the word {partial_string}: ") == choice:
    print("You survived!")
else:
    print("You lost!")
