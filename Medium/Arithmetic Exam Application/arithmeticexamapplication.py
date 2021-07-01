operation = input().split()
a, b = int(operation[0]), int(operation[2])
if operation[1] == "+":
    print(a + b)
elif operation[1] == "-":
    print(a - b)
elif operation[1] == "*":
    print(a * b)
