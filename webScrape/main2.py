from  bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web = response.text

soup = BeautifulSoup(yc_web, "html.parser")

title_text = soup.find_all(name="span", class_="titleline")
article_texts = []
article_links = []

for title  in title_text:
    anchor = title.find("a")
    text = anchor.getText()
    article_texts.append(text)
    link = anchor.get("href")
    article_links.append(link)
    
article_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]


print(article_texts)
print(article_links)
print(article_upvote)