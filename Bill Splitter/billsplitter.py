import random

n = int(input("Enter the number of friends joining (including you):\n"))
if n > 0:
    print()
    print("Enter the name of every friend (including you), each on a new line:")
    names = [input() for _ in range(n)]
    bill = int(input("\nEnter the total bill value:\n"))
    share = round(bill / n, 2)
    friends = dict.fromkeys(names, share)
    print('\nDo you want to use the "Who is lucky?" feature? Write Yes / No:')
    if input() == "Yes":
        print(f"\n{random.choice(names)} is the lucky one!")
    else:
        print("\nNo one is going to be lucky")
else:
    print("\nNo one is joining for the party")
