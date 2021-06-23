import random

binary_digits = []
while True:
    in_str = input("Print a random string containing 0 or 1:\n\n")
    binary_digits.extend([c for c in in_str if c in ("0", "1")])
    length = len(binary_digits)
    if length < 100:
        print(f"Current data length is {length}, {100 - length} symbols left")
    else:
        break
binary_string = "".join(binary_digits)
print(f"\nFinal data string:\n{binary_string}\n")

counts = {"000": [0, 0], "001": [0, 0], "010": [0, 0], "011": [0, 0],
          "100": [0, 0], "101": [0, 0], "110": [0, 0], "111": [0, 0]}
for i in range(len(binary_string) - 3):
    digit = int(binary_string[i + 3])
    counts[binary_string[i:i + 3]][digit] += 1

test_str = input("\nPlease enter a test string containing 0 or 1:\n\n")
total = len(test_str) - 3
correct = 0
prediction = random.choice("01") + random.choice("01") + random.choice("01")
for i in range(total):
    triad = test_str[i:i + 3]
    if counts[triad][0] > counts[triad][1]:
        prediction += "0"
    elif counts[triad][0] < counts[triad][1]:
        prediction += "1"
    else:
        prediction += random.choice("01")
    correct += prediction[i + 3] == test_str[i + 3]
print(f"prediction:\n{prediction}")
print(f"Computer guessed right {correct} out of {total} symbols", end="")
print(f" ({correct / total:.2%})")
