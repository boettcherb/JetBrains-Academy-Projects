flashcards = []


def get_option(prompt, min_option, max_option):
    while True:
        print(prompt)
        option = input()
        try:
            if min_option <= int(option) <= max_option:
                return int(option)
        except ValueError:
            pass
        print(f"{option} is not an option")


def get_flashcard():
    global flashcards
    question, answer = "", ""
    while not question:
        question = input("Question:\n")
    while not answer:
        answer = input("Answer:\n")
    flashcards.append((question, answer))


def add_flashcards():
    prompt = "1. Add a new flashcard\n2. Exit"
    while True:
        option = get_option(prompt, 1, 2)
        if option == 1:
            print()
            get_flashcard()
        elif option == 2:
            break
        print()


def practice_flashcards():
    global flashcards
    if not flashcards:
        print("\nThere is no flashcard to practice!")
        return
    for card in flashcards:
        print(f"\nQuestion: {card[0]}")
        print('Please press "y" to see the answer or press "n" to skip:')
        choice = input()
        if choice == "y":
            print(f"\nAnswer: {card[1]}")
        else:
            print()


def main():
    prompt = "1. Add flashcards\n2. Practice flashcards\n3. Exit"
    while True:
        option = get_option(prompt, 1, 3)
        if option == 1:
            print()
            add_flashcards()
        elif option == 2:
            practice_flashcards()
        elif option == 3:
            break
        print()
    print("\nBye!")


if __name__ == "__main__":
    main()
