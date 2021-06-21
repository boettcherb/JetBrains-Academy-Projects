n = int(input("Enter the number of friends joining (including you):\n"))
if n > 0:
    print()
    print("Enter the name of every friend (including you), each on a new line:")
    friends = dict.fromkeys([input() for _ in range(0, n)], 0)
    print("\n" + str(friends))
else:
    print("\nNo one is joining for the party")