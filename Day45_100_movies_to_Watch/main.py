from bs4 import BeautifulSoup
import requests

URL = "https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(URL)
web_html = response.text

soup = BeautifulSoup(web_html, "html.parser")
movies = soup.find_all(name="h3")
print(movies)
movie_titles = [movie.getText() for movie in movies]

all_movies = movie_titles[::-1]

with open("movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")
