import random


def find_letter(string, letter):
    """Return a set of all indexes of 'letter' in 'string'"""
    return {i for i, c in enumerate(string) if c == letter}


def main():
    print("H A N G M A N")
    word = random.choice(("python", "java", "kotlin", "javascript"))
    display = list("-" * len(word))
    letters_to_guess = set(word)
    lives = 8
    while lives > 0:
        print("\n" + "".join(display))
        if len(letters_to_guess) == 0:
            print("You guessed the word!")
            break
        letter = input("Input a letter: ")
        if letter not in letters_to_guess:
            lives -= 1
            print("No improvements" if letter in word else
                  "That letter doesn't appear in the word")
        else:
            letters_to_guess.remove(letter)
            for index in find_letter(word, letter):
                display[index] = letter
    print("You lost!" if lives == 0 else "You survived!")


if __name__ == "__main__":
    main()
