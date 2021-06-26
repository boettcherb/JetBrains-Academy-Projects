import argparse
import math


def is_pos_num(x, try_float):
    if x is None:
        return False
    try:
        x_num = float(x) if try_float else int(x)
        return x_num >= 0
    except ValueError:
        return False


def valid_args(t_, p_, n_, i_, a_):
    if (t_ != "diff" and t_ != "annuity") or not is_pos_num(i_, True):
        return False
    count = (p_ is not None) + (n_ is not None) + (a_ is not None)
    if (t_ == "diff" and a_ is not None) or count != 2:
        return False
    if p_ is not None and not is_pos_num(p_, False):
        return False
    if n_ is not None and not is_pos_num(n_, False):
        return False
    if a_ is not None and not is_pos_num(a_, False):
        return False
    return True


parser = argparse.ArgumentParser()
parser.add_argument("--type")
parser.add_argument("--principal")
parser.add_argument("--periods")
parser.add_argument("--interest")
parser.add_argument("--payment")
args = parser.parse_args()

t = args.type
p = args.principal
n = args.periods
i = args.interest
a = args.payment

if not valid_args(t, p, n, i, a):
    print("Incorrect parameters")
else:
    i = float(i) / 1200
    a = int(a) if a else None
    p = int(p) if p else None
    n = int(n) if n else None
    if t == "diff":
        total_payment = 0
        for m in range(1, n + 1):
            payment = math.ceil(p / n + i * (p - (p * (m - 1)) / n))
            total_payment += payment
            print(f"Month {m}: payment is {payment}")
        print(f"\nOverpayment = {total_payment - p}")
    else:
        if not p:
            p = math.floor(a / ((i * (1 + i) ** n) / ((1 + i) ** n - 1)))
            print(f"Your loan principal = {p}!")
        elif not a:
            a = math.ceil(p * (i * (1 + i) ** n) / ((1 + i) ** n - 1))
            print(f"Your monthly payment = {a}!")
        else:
            n = math.ceil(math.log(a / (a - i * p), 1 + i))
            years = n // 12
            months = n % 12
            time = "" if years == 0 else f"{years} years"
            if years and months:
                time += " and "
            time += f"{months} months" if months else ""
            print(f"It will take {time} to repay this loan!")
        print(f"Overpayment = {a * n - p}")
