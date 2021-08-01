while True:
    numbers = input()
    if numbers == "/exit":
        break
    elif numbers == "/help":
        print("The program calculates expressions using the + and - operators")
    elif numbers != "":
        expression = numbers.split()
        result = int(expression[0])
        for i in range(len(expression) // 2):
            op = expression[i * 2 + 1]
            number = int(expression[i * 2 + 2])
            result += number if op == "+" or len(op) % 2 == 0 else -number
        print(result)
print("Bye!")
