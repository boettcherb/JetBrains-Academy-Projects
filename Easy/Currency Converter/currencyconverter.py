import requests

cache = {}


def setup_cache(currency):
    exchange_data = query_float_rates(my_currency)
    if currency.lower() != "usd":
        cache["usd"] = exchange_data["usd"]["rate"]
    if currency.lower() != "eur":
        cache["eur"] = exchange_data["eur"]["rate"]


def check_cache(currency):
    print("Checking the cache...")
    return cache.get(currency)


def query_float_rates(currency):
    r = requests.get(f"http://www.floatrates.com/daily/{currency}.json")
    return r.json()


def get_exchange_rate(currency, new_currency):
    rate = check_cache(new_currency)
    if not rate:
        print("Sorry, but it is not in the cache!")
        data = query_float_rates(currency)
        cache[new_currency] = data[new_currency]["rate"]
        return data[new_currency]["rate"]
    print("Oh! It is in the cache!")
    return rate


my_currency = input()
setup_cache(my_currency)
exchange_currency = input()
while exchange_currency != "":
    amount = float(input())
    exchange_rate = get_exchange_rate(my_currency, exchange_currency.lower())
    new_amount = round(amount * exchange_rate, 2)
    print(f"You received {new_amount} {exchange_currency}.")
    exchange_currency = input()
