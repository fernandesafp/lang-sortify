# LangSortify
Separates songs in a Spotify playlist by language.

## Install the required libraries
Look up requirements.txt and run `pip install -r requirements.txt`.

Alternatively:
```console
pip install langdetect
pip install iso639
pip install lyricsgenius
pip install spotipy
```

## Export environment variables
Run this with your credentials in your environment
```console
export SPOTIPY_CLIENT_ID='your_spotify_client_id'
export SPOTIPY_CLIENT_SECRET='your_spotify_client_secret'
export SPOTIPY_REDIRECT_URI='your_genius_redirect_uri'
export GENIUS_ACCESS_TOKEN='your_genius_access_token'
```
## Inputs
Two windows will request the Spotify URI and if user wants to get language from the song lyrics.

<img src="/screenshots/spotify_uri.png" alt="Spotify URI window." width="250"/>

<img src="/screenshots/genius_window.png" alt="Genius search window." width="250"/>

## LangSortify finished
New playlists should show sorted by language.

![Sorted playlists.](/screenshots/sorted_playlists.png?raw=true)

Note: Although looking at the song name or album can be enough, because some songs were sung in another language with English titles, I decided to add language detection of their lyrics.
