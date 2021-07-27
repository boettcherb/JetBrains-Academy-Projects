import random
import sqlite3


def get_account_number(con):
    while True:
        account_num = str(random.randint(0, 999999999))
        q = f"SELECT * FROM card WHERE number = '{account_num}';"
        if not con.cursor().execute(q).fetchall():
            return account_num


def get_pin():
    pin = str(random.randint(0, 9999))
    return "0" * (4 - len(pin)) + pin


def get_checksum(card_num):
    nums = [int(d) if i % 2 else int(d) * 2 for i, d in enumerate(card_num)]
    digit_sum = sum(n if n < 10 else n - 9 for n in nums)
    return str((10 - digit_sum % 10) % 10)


def create_account(con):
    cur = con.cursor()
    card_id = cur.execute("SELECT MAX(id) from card;").fetchone()[0]
    card_id = (-1 if card_id is None else card_id) + 1
    account_num = get_account_number(con)
    card_num = "400000" + "0" * (9 - len(account_num)) + account_num
    card_num = card_num + get_checksum(card_num)
    pin = get_pin()
    cur.execute(f"INSERT INTO card (id, number, pin) "
                f"VALUES ({card_id}, '{card_num}', '{pin}');")
    con.commit()
    return card_num, pin


def login(con, card_num, pin):
    q = f"SELECT id FROM card WHERE number = '{card_num}' AND pin = '{pin}';"
    res = con.cursor().execute(q).fetchone()
    return None if not res else res[0]


def get_balance(con, card_id):
    q = f"SELECT balance FROM card WHERE id = {card_id};"
    return con.cursor().execute(q).fetchone()[0]


def main():
    con = sqlite3.connect("card.s3db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS card (id INTEGER, number TEXT, "
                "pin TEXT, balance INTEGER DEFAULT 0);")
    while True:
        action = input("1. Create an account\n2. Log into account\n0. Exit\n")
        if action == "1":
            card_number, pin = create_account(con)
            print("\nYour card has been created")
            print(f"Your card number:\n{card_number}")
            print(f"Your card pin:\n{pin}\n")
        elif action == "2":
            card_number = input("\nEnter your card number:\n")
            pin = input("Enter your pin:\n")
            account_id = login(con, card_number, pin)
            if account_id is None:
                print("\nWrong card number or PIN!\n")
            else:
                print("\nYou have successfully logged in!\n")
                while True:
                    choice = input("1. Balance\n2. Log out\n0. Exit\n")
                    if choice == "0":
                        print("\nBye!")
                        return
                    elif choice == "1":
                        print(f"\nBalance: {get_balance(con, account_id)}\n")
                    elif choice == "2":
                        print("\nYou have successfully logged out!\n")
                        break
        elif action == "0":
            print("\nBye!")
            return


if __name__ == "__main__":
    main()
