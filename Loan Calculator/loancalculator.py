import math

loan_principal = int(input("Enter the loan principal:\n"))
print("What do you want to calculate?")
print('type "m" for number of monthly payments,')
print('type "p" for the monthly payment')

if input() == "m":
    payment = int(input("Enter the monthly payment:\n"))
    months = math.ceil(loan_principal / payment)
    s = "s" if months > 1 else ""
    print(f"\nIt will take {months} month{s} to repay the loan")
else:
    months = int(input("Enter the number of months:\n"))
    payment = math.ceil(loan_principal / months)
    print(f"\nYour monthly payment = {payment}", end="")
    if loan_principal % payment != 0:
        last_payment = loan_principal - payment * (months - 1)
        print(f" and the last payment = {last_payment}.", end="")
    print()
