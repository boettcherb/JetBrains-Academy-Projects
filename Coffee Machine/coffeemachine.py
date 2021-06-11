water = 400
milk = 540
beans = 120
cups = 9
money = 550


def print_contents():
    global water, milk, beans, cups, money
    print("The coffee machine has:")
    print(water, "of water")
    print(milk, "of milk")
    print(beans, "of coffee beans")
    print(cups, "of disposable cups")
    print(money, "of money")


def get_action():
    print("Write action (buy, fill, take, remaining, exit):")
    return input()


def take():
    global money
    print("I gave you $", money)
    money = 0


def fill():
    global water, milk, beans, cups, money
    print("Write how many ml of water you want to add:")
    water += int(input())
    print("Write how many ml of milk you want to add:")
    milk += int(input())
    print("Write how many grams of coffee beans you want to add:")
    beans += int(input())
    print("Write how many disposable coffee cups you want to add:")
    cups += int(input())


def buy():
    global water, milk, beans, cups, money
    coffee = [[250, 0, 16, 4], [350, 75, 20, 7], [200, 100, 12, 6]]
    print("What do you want to buy? 1 - espresso, 2 - latte, "
          + "3 - cappuccino, back - to main menu:")
    coffee_type = input()
    if coffee_type == "back":
        return
    coffee_type = int(coffee_type) - 1
    if water < coffee[coffee_type][0]:
        print("Sorry, not enough water!")
    elif milk < coffee[coffee_type][1]:
        print("Sorry, not enough milk!")
    elif beans < coffee[coffee_type][2]:
        print("Sorry, not enough coffee beans!")
    elif cups < 1:
        print("Sorry, not enough cups!")
    else:
        print("I have enough resources, making you a coffee!")
        water -= coffee[coffee_type][0]
        milk -= coffee[coffee_type][1]
        beans -= coffee[coffee_type][2]
        money += coffee[coffee_type][3]
        cups -= 1


action = get_action()
while action != "exit":
    if action == "remaining":
        print_contents()
    elif action == "buy":
        buy()
    elif action == "fill":
        fill()
    elif action == "take":
        take()
    print()
    action = get_action()
