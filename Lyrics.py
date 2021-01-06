import os
import lyricsgenius as lg

def get_lyrics(genius, track):
    artists = track[0]
    song_name = track[1].split('-')[0]

    for artist in artists:
        try:
            song = genius.search_song(song_name, artist)
            lyrics = song.lyrics.replace('\n', '. ')
            break
        except:
            lyrics = 'unknown'

    return lyrics

def get_tracks_lyrics(tracks):
    GENIUS_CLIENT_ID = os.getenv('GENIUS_ACCESS_TOKEN')
    genius = lg.Genius(GENIUS_CLIENT_ID, skip_non_songs=True, remove_section_headers=True)

    tracks_with_lyrics = []
    for track in tracks:
        artists = track[0]
        song_name = track[1]
        album = track[2]
        song_uri = track[3]
        lyrics = get_lyrics(genius, track)
        tracks_with_lyrics.append([artists, song_name, album, song_uri, lyrics])

    return tracks_with_lyrics