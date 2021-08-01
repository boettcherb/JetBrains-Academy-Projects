while True:
    numbers = input()
    if numbers == "/exit":
        break
    if numbers != "":
        print(sum(int(x) for x in numbers.split()))
print("Bye!")
