import requests
from bs4 import BeautifulSoup
response = requests.get("https://news.ycombinator.com/")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
articles = soup.find_all(class_="titleline")
for article in articles:
    link = article.find("a")
    if link:
        print(f"Title: {link.getText()}")
        print(f"Link: {link.get('href')}")
        upvote = soup.find_all(name="span", class_="score").getText()
        print(f"Upvotes: {upvote}")
        print('-'*50)
