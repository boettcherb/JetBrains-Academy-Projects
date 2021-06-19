import math

print("What do you want to calculate?")
print('type "n" for number of monthly payments,')
print('type "a" for annuity monthly payment amount,')
print('type "p" for loan principal:')
letter = input()
if letter == "n":
    p = float(input("Enter the loan principal:\n"))
    a = float(input("Enter the monthly payment:\n"))
    i = float(input("Enter the loan interest:\n")) / 1200
    n = math.ceil(math.log(a / (a - i * p), 1 + i))
    years = n // 12
    time = ("" if years == 0 else f"{years} years and ") + f"{n % 12} months"
    print(f"It will take {time} to repay this loan!")
elif letter == "a":
    p = float(input("Enter the loan principal:\n"))
    n = float(input("Enter the number of periods:\n"))
    i = float(input("Enter the loan interest:\n")) / 1200
    a = p * (i * (1 + i) ** n) / ((1 + i) ** n - 1)
    print(f"Your monthly payment = {math.ceil(a)}!")
elif letter == "p":
    a = float(input("Enter the monthly payment:\n"))
    n = float(input("Enter the number of periods:\n"))
    i = float(input("Enter the loan interest:\n")) / 1200
    p = a / ((i * (1 + i) ** n) / ((1 + i) ** n - 1))
    print(f"Your loan principal = {round(p)}!")
