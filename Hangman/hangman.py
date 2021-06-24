import random


def find_letter(string, letter):
    """Return a set of all indexes of 'letter' in 'string'"""
    return {i for i, c in enumerate(string) if c == letter}


def main():
    print("H A N G M A N")
    word = random.choice(("python", "java", "kotlin", "javascript"))
    display = list("-" * len(word))
    for _ in range(8):
        print("\n" + "".join(display))
        letter = input("Input a letter: ")
        if letter not in word:
            print("That letter doesn't appear in the word")
        else:
            for index in find_letter(word, letter):
                display[index] = letter
    print("\nThanks for playing!\nWe'll see how you did in the next stage")


if __name__ == "__main__":
    main()
