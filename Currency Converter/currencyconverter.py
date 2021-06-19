import requests

r = requests.get(f"http://www.floatrates.com/daily/{input()}.json")
json_data = r.json()
print(json_data["usd"])
print(json_data["eur"])
