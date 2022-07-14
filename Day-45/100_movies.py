import requests
from bs4 import BeautifulSoup
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
movies_web = response.text
soup = BeautifulSoup(movies_web, "html.parser",)
all_movie_list = soup.find_all(name="h3", class_="title")
movie_titles = [title.getText() for title in all_movie_list]
movies = movie_titles[::-1]

with open("movies.txt", "w", encoding="utf8") as file:
    for movie in movies:
        file.write(f"{movie}\n")
