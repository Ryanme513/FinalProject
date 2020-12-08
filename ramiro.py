import random
import re
import webbrowser

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

credentials = SpotifyClientCredentials(client_id='d704a26dc6874b4983414f5baf910c4d', client_secret='41e7c1ebe3f24235b8ba0889ff267af8')
spotify = spotipy.Spotify(client_credentials_manager=credentials)


def choose_index(options):
  '''Displays a numbered list of `options` to the user and prompts them to select one.'''
  for i, option in enumerate(options, 1):
    print(f'{i}. {option}')
  while True:
    response = input(
      f'Please enter a number from 1 to {len(options)} to select a artist or song, or leave blank to let me choose! ')
    if not response:
      return random.randrange(len(options))
    try: index = int(response)
    except: continue
    if index > 0 and index <= len(options):
      return index - 1

def play_song(tracks):
  track_titles = [t['artists'][0]['name'] + ' - ' + t['name'] for t in tracks]
  print(f'I found a few songs from ARTIST for you:')
  track = tracks[choose_index(track_titles)]
  print(f'Listening to {track["name"]} by {track["artists"][0]["name"]}. Enjoy your new song and share with your friends :)')
  webbrowser.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open(track['external_urls']['spotify'])


artists = {
    'Marshmellow':'https://open.spotify.com/artist/64KEffDW9EtZ1y2vBYgq8T',
    'Khalid':'https://open.spotify.com/artist/6LuN9FCkKOj5PcnpouEgny',
    'Ariana Grande':'https://open.spotify.com/artist/66CXWjxzNUsdJxJ2JdwvnR',
    'Cardi B':'https://open.spotify.com/artist/4kYSro6naA4h99UJvo89HB',
    'Ed Sheeran':'https://open.spotify.com/artist/6eUKZXaKkcviH0Ku9w2n3V',
    'Justin Bieber':'https://open.spotify.com/artist/1uNFoZAHBGtllmzznpCI3s',
    'Dua Lipa':'https://open.spotify.com/artist/6M2wZ9GZgrQXHCFfjv46we',
    'J Balvin':'https://open.spotify.com/artist/1vyhD5VmyZ7KMfW5gqLgo5',
    'Drake':'https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4',
    'The Weeknd':'https://open.spotify.com/artist/1Xyo4u8uXC1ZmMpatF05PJ'
}



# print(choose_index(artists))
def top_artist():
  artists_names = list(artists.keys())
  artist_name_index = choose_index(artists_names)
  chosen_artist = artists_names[artist_name_index]
  artist_id = artists[chosen_artist]
  # webbrowser.open(track['external_urls']['spotify'])

  # response = input('Which artist would you like to see?')
  x = spotify.artist_top_tracks(artist_id=artist_id)
  play_song(x['tracks'])
  
top_artist()