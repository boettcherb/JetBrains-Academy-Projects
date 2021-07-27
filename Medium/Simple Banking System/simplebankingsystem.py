import random


class Account:
    all_accounts = []

    @staticmethod
    def get_account(card_number, pin):
        for acct in Account.all_accounts:
            if acct.card_number == card_number and acct.pin == pin:
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
        self.pin, self.card_number = 0, 0
        self.set_pin()
        self.set_card_number()
        self.balance = 0
        Account.all_accounts.append(self)

    def set_pin(self):
        pin = str(random.randint(0, 9999))
        self.pin = "0" * (4 - len(pin)) + pin

    def set_card_number(self):
        account_num = str(self.account_number)
        card_num = "400000" + "0" * (9 - len(account_num)) + account_num
        self.card_number = card_num + str(self.get_check_sum(card_num))

    def get_check_sum(self, card_num):
        digit_sum = 0
        for i, d in enumerate(card_num):
            d = int(d)
            if i % 2 == 0:
                d = d * 2 if d < 5 else d * 2 - 9
            digit_sum += d
        return (10 - digit_sum % 10) % 10


def main():
    while True:
        action = input("1. Create an account\n2. Log into account\n0. Exit\n")
        if action == "1":
            account = Account()
            print("\nYour card has been created")
            print(f"Your card number:\n{account.card_number}")
            print(f"Your card pin:\n{account.pin}\n")
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
