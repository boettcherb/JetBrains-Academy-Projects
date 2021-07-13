import requests


def main():
    r = requests.get(input("Input the URL:\n"))
    if r.status_code == 200:
        content = r.json().get("content", "")
        if content:
            print(content)
            return
    print("Invalid quote resource!")


if __name__ == "__main__":
    main()
