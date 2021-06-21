n = int(input("Enter the number of friends joining (including you):\n"))
if n > 0:
    print()
    print("Enter the name of every friend (including you), each on a new line:")
    names = [input() for _ in range(n)]
    bill = int(input("\nEnter the total bill value:\n"))
    share = round(bill / n, 2)
    print("\n" + str(dict.fromkeys(names, share)))
else:
    print("\nNo one is joining for the party")
