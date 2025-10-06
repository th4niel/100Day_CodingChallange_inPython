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

largest_number = max(article_upvote)
index_number = article_upvote.index(largest_number)
print(article_texts[index_number])
print(article_links[index_number])
print(largest_number)


# print(article_texts)
# print(article_links)
# print(article_upvote)