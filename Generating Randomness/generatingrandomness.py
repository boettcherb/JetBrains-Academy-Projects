from random import choice


def process_input(input_string):
    return "".join([c for c in input_string if c in "01"])


def get_prediction(input_string, frequencies):
    ai_prediction = ""
    correct = 0
    if len(input_string) > 3:
        ai_prediction += choice("01") + choice("01") + choice("01")
        for i in range(len(input_string) - 3):
            triad = input_string[i:i + 3]
            if frequencies[triad][0] > frequencies[triad][1]:
                ai_prediction += "0"
            elif frequencies[triad][0] < frequencies[triad][1]:
                ai_prediction += "1"
            else:
                ai_prediction += choice("01")
            correct += ai_prediction[i + 3] == input_string[i + 3]
    return ai_prediction, correct


def main():
    # Get the data string of > 100 characters to train the AI
    print("Please give AI some data to learn...")
    binary_string = ""
    while len(binary_string) < 100:
        length = len(binary_string)
        print(f"Current data length is {length}, {100 - length} symbols left")
        print("Print a random string containing 0 or 1:\n")
        binary_string += process_input(input())
    print(f"\nFinal data string:\n{binary_string}\n")

    # Count the frequency of digits after each triad for making predictions
    counts = {"000": [0, 0], "001": [0, 0], "010": [0, 0], "011": [0, 0],
              "100": [0, 0], "101": [0, 0], "110": [0, 0], "111": [0, 0]}
    for i in range(len(binary_string) - 3):
        digit = int(binary_string[i + 3])
        counts[binary_string[i:i + 3]][digit] += 1

    # Game loop. Ask for a string, make a prediction, and update user_money
    user_money = 1000
    print(f"You have ${user_money}. Every time the system successfully "
          f"predicts your next press, you lose $1.\nOtherwise, you earn $1. "
          f"Print \"enough\" to leave the game. Let's go!")
    while True:
        print("\nPrint a random string containing 0 or 1:")
        string = input()
        if string == "enough":
            break
        prediction, num_correct = get_prediction(process_input(string), counts)
        if prediction != "":
            print(f"prediction:\n{prediction}\n")
            total = len(prediction) - 3
            print(f"Computer guessed right {num_correct} out of {total} "
                  f"symbols ({num_correct / total:.2%})")
            user_money = user_money - num_correct + total - num_correct
            print(f"Your capital is now ${user_money}")
    print("Game over!")


if __name__ == "__main__":
    main()
