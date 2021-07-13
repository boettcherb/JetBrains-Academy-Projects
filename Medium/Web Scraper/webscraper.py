import requests
from bs4 import BeautifulSoup
import string
import os


def get_article_contents(article_link):
    r = requests.get(article_link)
    soup = BeautifulSoup(r.content, "html.parser")
    lines = soup.find("div", {"class": "c-article-body"})
    if lines is None:
        lines = soup.find("div", {"class": "article-item__body"})
    lines = lines.text.splitlines()
    return "".join([line.strip() for line in lines if line != ""])


def main():
    num_pages = int(input())
    article_type = input()
    url = "https://www.nature.com/nature/articles"
    for page in range(num_pages):
        directory = f"Page_{page + 1}"
        os.mkdir(directory)
        r = requests.get(url + f"?page={page + 1}")
        soup = BeautifulSoup(r.content, "html.parser")
        articles = soup.find_all("article")
        for article in articles:
            t = article.find("span", {"data-test": "article.type"}).find("span")
            if t.text == article_type:
                link_tag = article.find("a")
                link = "https://nature.com" + link_tag.get("href")
                title = link_tag.text
                for char in string.punctuation:
                    title = title.replace(char, "")
                file_name = directory + "/" + title.replace(" ", "_") + ".txt"
                with open(file_name, "w", encoding="utf-8") as f:
                    print(get_article_contents(link), file=f)


if __name__ == "__main__":
    main()
