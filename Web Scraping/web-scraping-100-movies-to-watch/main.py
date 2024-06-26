import requests
from bs4 import BeautifulSoup


URL = "https://www.empireonline.com/movies/features/best-movies-2/"
URL_BBC = "https://www.bbc.com/culture/article/20160819-the-21st-centurys-100-greatest-films"

response = requests.get(URL)
website_html = response.text


soup = BeautifulSoup(website_html, "html.parser")

all_movies = soup.find_all(name="h3", class_="listicleItem_listicle-item__title__BfenH")


movie_titles = [movie.getText() for movie in all_movies]
movies = movie_titles[::-1]

with open("movies_archive.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")

#BBC
response = requests.get(URL_BBC)
website_html = response.text


soup = BeautifulSoup(website_html, "html.parser")
# bbc = soup.find(name="div", class_="sc-43e6b7ba-0 bWSguZ")
# print(bbc)
bbc_movies = soup.find_all(name='p', class_="sc-eb7bd5f6-0 fYAfXe")
bbc_movie_titles = [movie.getText() for movie in bbc_movies]
bbc_movies = bbc_movie_titles[::-1]

with open("movies_bbc.txt", mode="w", encoding="utf-8") as file:
    for movie in bbc_movies:
        file.write(f"{movie}\n")
