import random


def get_answer():
    while True:
        try:
            return int(input())
        except ValueError:
            print("Incorrect format.")


def arithmetic_task():
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


def main():
    num_correct = 0
    for i in range(5):
        correct = arithmetic_task()
        print("Right!" if correct else "Wrong!")
        num_correct += correct
    print(f"Your mark is {num_correct}/5")


if __name__ == "__main__":
    main()
