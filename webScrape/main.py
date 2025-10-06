from bs4 import BeautifulSoup

with open('./webScrape/index.html',) as file:
    content = file.read()
    
soup = BeautifulSoup(content, "html.parser")
# print(soup.body.string)

all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)

# for tag in all_anchor_tags:
#     print(tag.get("href"))

##because there are multiple h1 classes
# headig = soup.find(name="h1", id="website")
# print(headig)

# test = soup.find_all("h1", class_="name3")

# for t in test:
#     print(t.text)

form = soup.find("li", id="job")
print (form.text)

# form = soup.find("li", class_="asd")
# # absz = form.get("class")
# for f in form:
#     print(form.get("class"))

#============ SELECT (finding element by using css selector style)==========
# test = soup.select_one(selector="#name")
# print(test)

# a = soup.select("ul a")
# print(a)