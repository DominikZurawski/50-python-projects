import os
from datetime import datetime
import requests
from bs4 import BeautifulSoup

# SET SPOTIFY
import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials

scope = "user-library-read"
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id= os.environ["SPOTIPY_CLIENT_ID"],
        client_secret= os.environ["SPOTIPY_CLIENT_SECRET"],
        show_dialog=True,
        cache_path="token.txt"
    )
)

#sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
user = sp.current_user()['id']
#print(user)
results = sp.current_user_saved_tracks()

for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])


# SCRAPING 100 TOP SONGS

date = input("Which year do you want to travel to? type date in this format 'YYYY-MM-DD':  ")
# print(date[:4])
URL = f"https://www.billboard.com/charts/hot-100/{date}/"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, 'html.parser')

song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]

# with open(f"top-{date}.txt", mode="w") as file:
#     for song in song_names:
#         file.write(f"{song}\n")

# SEARCH SONGS ON SPOTIFY
song_uris = []
year = date[:4]
playlist = sp.user_playlist_create(user=user, name=f"{date} Hot 100", public=False)
print(playlist)
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        song_uris.append(result["tracks"]["items"][0]["uri"])
        print(result["tracks"]["items"][0]["uri"])
    except:
        print(f"{song} doesn't exist in Spotify. Skipped.")


sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)


