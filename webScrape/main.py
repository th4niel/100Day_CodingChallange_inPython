from bs4 import BeautifulSoup

with open('./webScrape/index.html',) as file:
    content = file.read()
    
soup = BeautifulSoup(content, "html.parser")
# print(soup.body.string)

all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)

# for tag in all_anchor_tags:
#     print(tag.get("href"))

# headig = soup.find(name="h1", id="website")
# print(headig)

# test = soup.find_all("h1", class_="name3")

# for t in test:
#     print(t.get("class"))


test = soup.select_one(selector="#name")
print(test)