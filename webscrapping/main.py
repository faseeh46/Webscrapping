import requests
from bs4 import BeautifulSoup

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
website_html = response.text
soup = BeautifulSoup(website_html, "html.parser")
all_movies = soup.find_all(name="h3", class_="listicleItem_listicle-item__title__BfenH")
top_movies = [movies.getText() for movies in all_movies]
movies = top_movies[::-1]

with open("top_movies.txt", "w") as file:
    for movie in movies:
        file.write(f"{movie} \n")
