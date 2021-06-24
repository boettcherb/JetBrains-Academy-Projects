import random

print("H A N G M A N")
words = ("python", "java", "kotlin", "javascript")
if input("Guess the word: ") == random.choice(words):
    print("You survived!")
else:
    print("You lost!")
