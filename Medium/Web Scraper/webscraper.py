import requests
from bs4 import BeautifulSoup
import string


def get_article_contents(article_link):
    r = requests.get(article_link)
    soup = BeautifulSoup(r.content, "html.parser")
    lines = soup.find("div", {"class": "c-article-body"}).text.splitlines()
    return "".join([line.strip() for line in lines if line != ""])


def main():
    r = requests.get("https://www.nature.com/nature/articles")
    soup = BeautifulSoup(r.content, "html.parser")
    articles = soup.find_all("article")
    for article in articles:
        t = article.find("span", {"data-test": "article.type"}).find("span")
        if t.text == "News":
            link_tag = article.find("a")
            link = "https://nature.com" + link_tag.get("href")
            title = link_tag.text
            for char in string.punctuation:
                title = title.replace(char, "")
            title = title.replace(" ", "_")
            with open(title + ".txt", "w", encoding="utf-8") as f:
                print(get_article_contents(link), file=f)


if __name__ == "__main__":
    main()
