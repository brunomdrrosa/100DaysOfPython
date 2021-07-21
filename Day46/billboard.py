from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests
import os

SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")

# Scraping Billboard 100
data = input("Você quer voltar no tempo para que dia? Digite a data no formato AAAA-MM-DD\n")
resposta = requests.get(f"https://www.billboard.com/charts/hot-100/{data}")

soup = BeautifulSoup(resposta.text, 'html.parser')
song_names_spans = soup.find_all("span", class_="chart-element__information__song")
song_names = [song.getText() for song in song_names_spans]

# Spotify Authentication
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

# Procurando a música no Spotify pelo títutlo
song_uris = []
year = data.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} não existe no Spotify.")

# Criando uma playlist privada no Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{data} Billboard 100", public=False)
print(playlist)

# Adicionando as músicas encontradas na playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
