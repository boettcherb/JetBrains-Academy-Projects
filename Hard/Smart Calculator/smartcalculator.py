from string import ascii_letters

variables = {}


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
        print("Invalid expression")
        return False
    for i, part in enumerate(parts):
        if i % 2 == 0 and get_value(part) is None:
            print("Unknown variable")
            return False
        if i % 2 == 1 and part != ("+" * len(part)) and part != ("-" * len(part)):
            print("Invalid expression")
            return False
    return True


def get_value(operand):
    try:
        return int(operand)
    except:
        return variables.get(operand, None)


def process_assignment(expression):
    if expression.count("=") != 1:
        print("Invalid assignment")
        return
    left, right = (e.strip() for e in expression.split("="))
    if any(c not in ascii_letters for c in left):
        print("Invalid identifier")
        return
    val = get_value(right)
    if val is None:
        if all(c in ascii_letters for c in right):
            print("Unknown variable")
        else:
            print("Invalid assignment")
    else:
        variables[left] = val


def main():
    while True:
        expression = input()
        if expression == "":
            continue
        elif expression[0] == "/":
            if process_command(expression) == "exit":
                break
        else:
            if expression.count("="):
                process_assignment(expression)
                continue
            if not valid_expression(expression):
                print("Invalid expression")
                continue
            expression = expression.split()
            result = get_value(expression[0])
            for i in range(len(expression) // 2):
                op = expression[i * 2 + 1]
                number = get_value(expression[i * 2 + 2])
                result += number if op == "+" or len(op) % 2 == 0 else -number
            print(result)
    print("Bye!")


if __name__ == "__main__":
    main()
