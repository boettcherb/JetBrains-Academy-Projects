import requests
from bs4 import BeautifulSoup


def main():
    r = requests.get(input())
    soup = BeautifulSoup(r.content, 'html.parser')
    head = soup.find('h1')
    desc = soup.find('p')
    rev = soup.find('span', text="User reviews")
    try:
        if "User reviews" in rev.text:
            print({"title": head.text, "description": desc.text})
    except AttributeError:
        print("Invalid movie page!")


if __name__ == "__main__":
    main()