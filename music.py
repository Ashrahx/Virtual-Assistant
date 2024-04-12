import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from googleapiclient.discovery import build

# Configuración de Spotify
spotify_client_id = os.getenv('SPOTIFY_CLIENT_ID')
spotify_client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')

# Configuración de YouTube
youtube_api_key = os.getenv('YOUTUBE_API_KEY')

def search_song_on_spotify(song_name):
    client_credentials_manager = SpotifyClientCredentials(client_id=spotify_client_id, client_secret=spotify_client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    results = sp.search(q=song_name, limit=1)
    if results['tracks']['items']:
        track = results['tracks']['items'][0]
        return f"Encontré la canción '{track['name']}' en Spotify. Puedes escucharla aquí: {track['external_urls']['spotify']}"
    else:
        return "No se encontró la canción en Spotify."

def search_song_on_youtube(song_name):
    youtube = build('youtube', 'v3', developerKey=youtube_api_key)

    request = youtube.search().list(
        part="snippet",
        maxResults=1,
        q=song_name
    )
    response = request.execute()

    if response['items']:
        video = response['items'][0]
        return f"Encontré la canción '{video['snippet']['title']}' en YouTube. Puedes verla aquí: https://www.youtube.com/watch?v={video['id']['videoId']}"
    else:
        return "No se encontró la canción en YouTube."
