import random

l1_format = "1 - simple operations with numbers 2-9"
l2_format = "2 - integral squares of 11-29"


def get_level():
    while True:
        print("Which level do you want? Enter a number:")
        print(l1_format)
        print(l2_format)
        level = input()
        if level == "1" or level == "2":
            return int(level)
        print("Incorrect format.")


def get_answer():
    while True:
        try:
            return int(input())
        except ValueError:
            print("Incorrect format.")


def arithmetic_task(level):
    if level == 1:
        a = random.randint(2, 9)
        b = random.randint(2, 9)
        operator = random.choice("+-*")
        print(f"{a} {operator} {b}")
        answer = get_answer()
        if operator == "+":
            return a + b == answer
        elif operator == "-":
            return a - b == answer
        elif operator == "*":
            return a * b == answer
    else:
        num = random.randint(11, 29)
        print(num)
        return get_answer() == num * num


def main():
    level = get_level()
    num_correct = 0
    for i in range(5):
        correct = arithmetic_task(level)
        print("Right!" if correct else "Wrong!")
        num_correct += correct
    print(f"Your mark is {num_correct}/5")
    print("Would you like to save your result to the file? Enter yes or no")
    user_input = input().lower()
    if user_input == "y" or user_input == "yes":
        name = input("What is your name?\n")
        f = open("results.txt", "a")
        form = l1_format if level == 1 else l2_format
        print(f"{name}: {num_correct}/5 in level {level} ({form})", file=f)
        f.close()
        print('The results are saved in "results.txt".')


if __name__ == "__main__":
    main()
