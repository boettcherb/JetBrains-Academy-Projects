import random

n = int(input("Enter the number of friends joining (including you):\n"))
if n > 0:
    print()
    print("Enter the name of every friend (including you), each on a new line:")
    names = [input() for _ in range(n)]
    bill = int(input("\nEnter the total bill value:\n"))
    print('\nDo you want to use the "Who is lucky?" feature? Write Yes / No:')
    if input() == "Yes":
        lucky_person = random.choice(names)
        print(f"\n{lucky_person} is the lucky one!\n")
        friends = dict.fromkeys(names, round(bill / (n - 1), 2))
        friends[lucky_person] = 0
        print(friends)
    else:
        print("\nNo one is going to be lucky\n")
        print(dict.fromkeys(names, round(bill / n, 2)))
else:
    print("\nNo one is joining for the party")
