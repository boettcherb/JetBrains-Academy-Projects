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
    print("Write action (buy, fill, take):")
    return input()


def take():
    global money
    print("I give you $", money)
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
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
    coffee_type = int(input()) - 1
    water -= coffee[coffee_type][0]
    milk -= coffee[coffee_type][1]
    beans -= coffee[coffee_type][2]
    money += coffee[coffee_type][3]
    cups -= 1

        
print_contents()
print()
action = get_action()
if action == "buy":
    buy()
elif action == "fill":
    fill()
elif action == "take":
    take()
print()
print_contents()
