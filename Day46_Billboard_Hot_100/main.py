from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy import SpotifyOAuth

print("In which year want to check the Billboard top 100")
date = input("Please insert the date in YYYY-MM-DD FORMAT\n")
URL = "https://www.billboard.com/charts/hot-100/"
response = requests.get(f"{URL}{date}")

soup = BeautifulSoup(response.text, "html.parser")
list_of_song = soup.find_all("span", class_="chart-element__information__song")
song_name = [song.getText() for song in list_of_song]
access_spotify = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id="0696c74e940b4c0aa5b546f21dc039fa",
        client_secret="f5b0962ab342431b8b46728409e2c3cb",
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = access_spotify.current_user()["id"]
print(user_id)

song_uris = []
year = date.split("-")[0]
for song in song_name:
    result = access_spotify.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped")

playlist = access_spotify.user_playlist_create(user=user_id, name=f"{date}Billboard 100", public=False)
print(playlist)
access_spotify.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
