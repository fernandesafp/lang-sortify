import SpotifyAPI, Lyrics, Languages
import sys
import tkinter
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo,showwarning

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
    #Opens input dialog to insert Spotify URI
    spotify_uri = request_spotify_uri()

    #Returns track array with Artists - Song name format
    tracks = SpotifyAPI.get_playlist_tracks(spotify_uri)

    #------------------------------------------------------------------------------
    #To do
    #Returns array with the tracks and lyrics
    tracks_with_lyrics = Lyrics.get_tracks_lyrics(tracks)

    #Returns array with the tracks and language based on their lyrics
    tracks_with_languages = Languages.get_lyrics_language(tracks_with_lyrics)

    #Creates playlists based on the language and adds tracks
    SpotifyAPI.sort_spotify_by_language(tracks_with_languages)
    #------------------------------------------------------------------------------