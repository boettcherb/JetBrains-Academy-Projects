binary_digits = []
while True:
    in_str = input("Print a random string containing 0 or 1:\n\n")
    binary_digits.extend([c for c in in_str if c in ("0", "1")])
    length = len(binary_digits)
    if length < 100:
        print(f"Current data length is {length}, {100 - length} symbols left")
    else:
        break
print("\nFinal data string:\n" + "".join(binary_digits))
