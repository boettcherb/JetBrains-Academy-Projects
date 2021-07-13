import requests


def main():
    r = requests.get(input())
    if r.status_code == 200:
        with open("source.html", "wb") as html_file:
            html_file.write(r.content)
            print("Content saved.")
    else:
        print(f"The URL returned {r.status_code}!")


if __name__ == "__main__":
    main()
