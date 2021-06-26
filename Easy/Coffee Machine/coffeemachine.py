class CoffeeMachine:
    states = ["get action", "fill water", "fill milk", "fill beans", "fill cups", "buy"]

    def __init__(self, water, milk, beans, cups, money):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money
        self.state = None
        self.get_action()

    def process_user_input(self, user_input):
        if self.state == "get action":
            if user_input == "exit":
                return 0
            if user_input == "remaining":
                self.print_contents()
            if user_input == "take":
                self.take()
            elif user_input == "fill":
                print()
                print("Write how many ml of water do you want to add:")
                self.state = "fill water"
            elif user_input == "buy":
                self.ask_coffee_type()
        elif self.state == "fill water":
            self.fill_water(int(user_input))
        elif self.state == "fill milk":
            self.fill_milk(int(user_input))
        elif self.state == "fill beans":
            self.fill_beans(int(user_input))
        elif self.state == "fill cups":
            self.fill_cups(int(user_input))
        elif self.state == "buy":
            self.buy(user_input)
        return 1

    def get_action(self):
        print("Write action (buy, fill, take, remaining, exit):")
        self.state = "get action"

    def print_contents(self):
        print()
        print("The coffee machine has:")
        print(self.water, "of water")
        print(self.milk, "of milk")
        print(self.beans, "of coffee beans")
        print(self.cups, "of disposable cups")
        print(self.money, "of money")
        print()
        self.get_action()

    def take(self):
        print()
        print(f"I gave you ${self.money}")
        self.money = 0
        print()
        self.get_action()

    def fill_water(self, water):
        self.water += water
        self.state = "fill milk"
        print("Write how many ml of milk do you want to add:")

    def fill_milk(self, milk):
        self.milk += milk
        self.state = "fill beans"
        print("Write how many grams of coffee beans do you want to add:")

    def fill_beans(self, beans):
        self.beans += beans
        self.state = "fill cups"
        print("Write how many disposable cups of coffee do you want to add:")

    def fill_cups(self, cups):
        self.cups += cups
        print()
        self.get_action()

    def ask_coffee_type(self):
        print()
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        self.state = "buy"

    def buy(self, coffee_type):
        coffee = [[250, 0, 16, 4], [350, 75, 20, 7], [200, 100, 12, 6]]
        if coffee_type != "back":
            coffee_type = int(coffee_type) - 1
            if self.water < coffee[coffee_type][0]:
                print("Sorry, not enough water!")
            elif self.milk < coffee[coffee_type][1]:
                print("Sorry, not enough milk!")
            elif self.beans < coffee[coffee_type][2]:
                print("Sorry, not enough coffee beans!")
            elif self.cups < 1:
                print("Sorry, not enough cups!")
            else:
                print("I have enough resources, making you a coffee!")
                self.water -= coffee[coffee_type][0]
                self.milk -= coffee[coffee_type][1]
                self.beans -= coffee[coffee_type][2]
                self.money += coffee[coffee_type][3]
                self.cups -= 1
        print()
        self.get_action()


coffee_machine = CoffeeMachine(400, 540, 120, 9, 550)
while coffee_machine.process_user_input(input()):
    continue
