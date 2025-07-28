# spotify_config.py
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

SPOTIPY_CLIENT_ID = "your_spotify_client_id"
SPOTIPY_CLIENT_SECRET = "your_spotify_client_secret"

def get_spotify_client():
    auth_manager = SpotifyClientCredentials(
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET
    )
    return spotipy.Spotify(auth_manager=auth_manager)

def get_songs_by_genre(genre, limit=5):
    sp = get_spotify_client()
    results = sp.search(q=f"genre:{genre}", type="track", limit=limit)
    tracks = []
    for item in results['tracks']['items']:
        tracks.append({
            "name": item['name'],
            "artist": item['artists'][0]['name'],
            "url": item['external_urls']['spotify']
        })
    return tracks
