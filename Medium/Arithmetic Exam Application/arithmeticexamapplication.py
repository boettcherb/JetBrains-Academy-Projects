import random

a = random.randint(2, 9)
b = random.randint(2, 9)
operator = random.choice("+-*")
print(f"{a} {operator} {b}")
answer = int(input())
if operator == "+":
    print("Right!" if a + b == answer else "Wrong!")
elif operator == "-":
    print("Right!" if a - b == answer else "Wrong!")
elif operator == "*":
    print("Right!" if a * b == answer else "Wrong!")
