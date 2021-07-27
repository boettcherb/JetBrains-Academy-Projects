import random


class Account:
    all_accounts = []

    @staticmethod
    def get_account(card_number, pin):
        for acct in Account.all_accounts:
            if acct.get_card_number() == card_number and acct.get_pin() == pin:
                return acct
        return None

    @staticmethod
    def get_new_account_number():
        while True:
            num = random.randint(0, 999999999)
            if not any(a.account_number == num for a in Account.all_accounts):
                return num

    def __init__(self):
        self.account_number = self.get_new_account_number()
        self.pin = random.randint(0, 9999)
        self.checksum = random.randint(0, 9)
        self.balance = 0
        Account.all_accounts.append(self)

    def get_card_number(self):
        an = str(self.account_number)
        an = "0" * (9 - len(an)) + an
        return "400000" + an + str(self.checksum)

    def get_pin(self):
        return "0" * (4 - len(str(self.pin))) + str(self.pin)


def main():
    while True:
        action = input("1. Create an account\n2. Log into account\n0. Exit\n")
        if action == "1":
            account = Account()
            print("\nYour card has been created")
            print(f"Your card number:\n{account.get_card_number()}")
            print(f"Your card pin:\n{account.get_pin()}\n")
        elif action == "2":
            card_number = input("\nEnter your card number:\n")
            pin = input("Enter your pin:\n")
            account = Account.get_account(card_number, pin)
            if account is None:
                print("\nWrong card number or PIN!")
            else:
                print("\nYou have successfully logged in!\n")
                while True:
                    choice = input("1. Balance\n2. Log out\n0. Exit\n")
                    if choice == "0":
                        print("\nBye!")
                        return
                    elif choice == "1":
                        print(f"\nBalance: {account.balance}\n")
                    elif choice == "2":
                        print("\nYou have successfully logged out!\n")
                        break
        elif action == "0":
            print("\nBye!")
            return


if __name__ == "__main__":
    main()
