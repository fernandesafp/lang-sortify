import sys
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import tkinter
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo,showwarning

def sort_tracks_by_language(tracks_with_languages):
    return tracks_with_languages

def get_lyrics_language(tracks_with_lyrics):
    return tracks_with_lyrics

def get_tracks_lyrics(tracks):
    return tracks

def get_playlist_tracks(spotify_uri):
    scope = 'user-library-read'

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

    results = sp.playlist_tracks(spotify_uri)
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])

    track_array = []
    for track in tracks:
        track_name = track['track']['name']
        artists_array = []
        for artist in track['track']['artists']:
            artists_array.append(artist['name'])
        track_artists = ', '.join(artists_array)
        track_array.append(track_artists + ' - ' + track_name)

    with open('spotify_tracks.txt', 'w') as f: #Temporarily writes a file with all the songs of the track
        for item in track_array:
            f.write("%s\n" % item)

    return track_array

def request_spotify_uri():
    main = tkinter.Tk()
    main.withdraw()
    spotify_uri = askstring('Playlist URI', 'What is the playlist URI?')
    if spotify_uri:
        return spotify_uri
    else:
        showwarning('Warning','No Spotify URI was provided. Closing...',)
        sys.exit(0)

if __name__ == "__main__":
    #Add to environment or include yourself:
    #SPOTIPY_CLIENT_ID='YOUR_CLIENT_ID'
    #SPOTIPY_CLIENT_SECRET='YOUR_CLIENT_SECRET'
    #SPOTIPY_REDIRECT_URI='YOUR_ADDED_REDIRECT_URI' #Example: http://127.0.0.1:9090

    #Opens input dialog to insert Spotify URI
    spotify_uri = request_spotify_uri()

    #Returns track array with Artists - Song name format
    tracks = get_playlist_tracks(spotify_uri)

    #------------------------------------------------------------------------------
    #To do
    #Returns array with the tracks and lyrics
    tracks_with_lyrics = get_tracks_lyrics(tracks)

    #Returns array with the tracks and language based on their lyrics
    tracks_with_languages = get_lyrics_language(tracks_with_lyrics)

    #Creates playlists based on the language and adds tracks
    sort_tracks_by_language(tracks_with_languages)
    #------------------------------------------------------------------------------