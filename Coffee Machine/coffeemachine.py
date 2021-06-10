print("Write how many ml of water the coffee machine has:")
water = int(input())
print("Write how many ml of milk the coffee machine has:")
milk = int(input())
print("Write how many grams of coffee beans the coffee machine has:")
coffee_beans = int(input())
print("Write how many cups of coffee you will need:")
requested = int(input())
possible = 0
while (water >= 200 and milk >= 50 and coffee_beans >= 15):
    possible += 1
    water -= 200
    milk -= 50
    coffee_beans -= 15
if possible < requested:
    print("No, I can make only " + str(possible) + " cups of coffee")
else:
    print("Yes, I can make that amount of coffee", end = "")
    if possible > requested:
        extra = str(possible - requested)
        print("(and even " + extra + " more than that)", end = "")
    print()
