from bs4 import BeautifulSoup

with open("website.html", encoding="utf8") as datafile:
    contents = datafile.read()

soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)
# print(soup.title.string)
# print(soup.prettify())
# print(soup.a)
all_anchor_tag = soup.find_all(name="a")
# print(all_anchor_tag)

# for tag in all_anchor_tag:
#     # print(tag.getText())
#     print(tag.get("href"))

# heading = soup.find(name="h1", id="name")
# print(heading)

# print(soup.find(name="h3", class_="heading"))

company_url = soup.select_one(selector="p a")
print(company_url)