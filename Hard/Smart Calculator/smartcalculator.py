from string import ascii_letters
from collections import deque


class Stack:
    def __init__(self):
        self.stack = deque()

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()

    def top(self):
        top_value = self.stack.pop()
        self.stack.append(top_value)
        return top_value

    def empty(self):
        return len(self.stack) == 0

    def __repr__(self):
        return str(list(self.stack))

    def __len__(self):
        return len(self.stack)


variables = {}


def process_command(command):
    if command == "/exit":
        return "exit"
    if command == "/help":
        print("Calculates expressions using the + and - operators")
    else:
        print("Unknown command")
    return "continue"


def get_value(operand):
    try:
        return int(operand)
    except ValueError:
        return variables.get(operand, None)


def check_parentheses(expression):
    depth = 0
    for c in expression:
        depth += c == "("
        depth -= c == ")"
        if depth < 0:
            return False
    return depth == 0


def parse_expression(expression):
    if not check_parentheses(expression):
        return "Invalid expression"
    while expression.count("++"):
        expression = expression.replace("++", "+")
    while expression.count("---"):
        expression = expression.replace("---", "-")
    while expression.count("--"):
        expression = expression.replace("--", "+")
    for op in "+-*/()":
        expression = expression.replace(op, f" {op} ")
    expression = expression.split()
    operand = True
    for i, part in enumerate(expression):
        if part in "()":
            continue
        if operand:
            value = get_value(part)
            if value is None:
                if any(c not in ascii_letters for c in part):
                    return "Invalid identifier"
                return "Unknown variable"
            expression[i] = value
        elif part not in "+-*/()":
            return "Invalid expression"
        operand = not operand
    return expression


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


def convert_to_postfix(prefix):
    precedence = {"+": 1, "-": 1, "*": 2, "/": 2}
    postfix = Stack()
    operators = Stack()
    for part in prefix:
        if isinstance(part, int):
            postfix.push(part)
        elif part == "(":
            operators.push(part)
        elif part == ")":
            while operators.top() != "(":
                postfix.push(operators.pop())
            operators.pop()
        elif part in "+-*/":
            while not operators.empty() and operators.top() != "(":
                if precedence[part] <= precedence[operators.top()]:
                    postfix.push(operators.pop())
                else:
                    break
            operators.push(part)
    while not operators.empty():
        postfix.push(operators.pop())
    return postfix


def get_operand(postfix):
    if isinstance(postfix.top(), int):
        return postfix.pop()
    return evaluate_postfix(postfix)


def evaluate_postfix(postfix):
    if len(postfix) == 1:
        return postfix.pop()
    operator = postfix.pop()
    right, left = get_operand(postfix), get_operand(postfix)
    if operator == "+":
        return left + right
    if operator == "-":
        return left - right
    if operator == "*":
        return left * right
    return left // right


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
            prefix = parse_expression(expression)
            if isinstance(prefix, str):
                print(prefix)
                continue
            print(evaluate_postfix(convert_to_postfix(prefix)))
    print("Bye!")


if __name__ == "__main__":
    main()
