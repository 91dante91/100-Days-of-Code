import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_SPOTIFY_ID = "example"
CLIENT_SPOTIFY_SECRET = "example"

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
response = requests.get("https://www.billboard.com/charts/hot-100/" + date)
soup = BeautifulSoup(response.text, "html.parser")
print(soup)
# song_names_span = soup.find_all(name="span", class_="chart-element__information__song text--truncate color--primary")
# song_names = [song.getText() for song in song_names_span]
#
# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_SPOTIFY_ID, client_secret=CLIENT_SPOTIFY_SECRET,
#                                                redirect_uri="http://example.com", scope="playlist-modify-private",
#                                                show_dialog=True, cache_path="Token.txt"))
# user_id = sp.current_user()["id"]
# print(user_id)
#
# song_uris = []
# year = date.split("-")[0]
# for song in song_names:
#     result = sp.search(q=f"track:{song} year:{year}", type="track")
#     try:
#         uri = result["tracks"]["items"][0]["uri"]
#         song_uris.append(uri)
#     except IndexError:
#         print(f"{song} doesn't exist in Spotify. Skipped.")
# playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
# print(playlist)
# sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
