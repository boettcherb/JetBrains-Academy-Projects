import random


def find_letter(string, letter):
    """Return a set of all indexes of 'letter' in 'string'"""
    return {i for i, c in enumerate(string) if c == letter}


def get_menu_choice():
    """Ask the user if they would like to play Hangman or quit the program."""
    menu_message = 'Type "play" to play the game, "exit" to quit: '
    menu_choice = input(menu_message)
    while menu_choice not in ("play", "exit"):
        menu_choice = input(menu_message)
    return menu_choice


def main():
    print("H A N G M A N")
    while get_menu_choice() != "exit":
        word = random.choice(("python", "java", "kotlin", "javascript"))
        display = list("-" * len(word))
        letters_to_guess = set(word)
        guessed_letters = set()
        lives = 8
        while lives > 0:
            print("\n" + "".join(display))
            if len(letters_to_guess) == 0:
                print(f"You guessed the word {word}!")
                break
            letter = input("Input a letter: ")
            if len(letter) != 1:
                print("You should input a single letter")
            elif not letter.islower():
                print("Please enter a lowercase English letter")
            elif letter in guessed_letters:
                print("You've already guessed this letter")
            elif letter not in letters_to_guess:
                lives -= 1
                print("That letter doesn't appear in the word")
                guessed_letters.add(letter)
            else:
                letters_to_guess.remove(letter)
                for index in find_letter(word, letter):
                    display[index] = letter
                guessed_letters.add(letter)
        print("You lost!\n" if lives == 0 else "You survived!\n")


if __name__ == "__main__":
    main()
