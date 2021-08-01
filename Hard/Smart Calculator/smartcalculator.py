while True:
    numbers = input()
    if numbers == "/exit":
        break
    elif numbers == "/help":
        print("The program calculates the sum of numbers")
    elif numbers != "":
        print(sum(int(x) for x in numbers.split()))
print("Bye!")
