from  bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web = response.text

soup = BeautifulSoup(yc_web, "html.parser")

title_text = soup.find_all(name="span", class_="titleline")

for title  in title_text:
    anchor = title.find("a")
    if anchor:
        print(anchor.getText())
        print(anchor.get("href"))
        print("-------")