def process_command(command):
    if command == "/exit":
        return "exit"
    if command == "/help":
        print("Calculates expressions using the + and - operators")
    else:
        print("Unknown command")
    return "continue"


def valid_expression(expression):
    parts = expression.split()
    if len(parts) % 2 == 0:
        return False
    for i, part in enumerate(parts):
        if i % 2 == 0:
            try:
                int(part)
            except ValueError:
                return False
        else:
            if part != ("+" * len(part)) and part != ("-" * len(part)):
                return False
    return True


def main():
    while True:
        expression = input()
        if expression == "":
            continue
        elif expression[0] == "/":
            if process_command(expression) == "exit":
                break
        else:
            if not valid_expression(expression):
                print("Invalid expression")
                continue
            expression = expression.split()
            result = int(expression[0])
            for i in range(len(expression) // 2):
                op = expression[i * 2 + 1]
                number = int(expression[i * 2 + 2])
                result += number if op == "+" or len(op) % 2 == 0 else -number
            print(result)
    print("Bye!")


if __name__ == "__main__":
    main()
