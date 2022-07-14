import requests
from bs4 import BeautifulSoup

response = requests.get(url="https://news.ycombinator.com/")
yc_webpage = response.text
# print(yc_webpage)

soup = BeautifulSoup(yc_webpage, "html.parser")
article_texts = []
article_links = []
articles = soup.find_all(name="a", class_="titlelink")
for article in articles:
    article_texts.append(article.get_text())
    article_links.append(article.get("href"))

article_points = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

largest_number = max(article_points)
largest_number_index = article_points.index(largest_number)
print(article_texts[largest_number_index])
print(article_links[largest_number_index])
print(largest_number)


