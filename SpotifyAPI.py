import spotipy
from spotipy.oauth2 import SpotifyOAuth

def get_playlist_tracks(spotify_uri):
    #Add to environment or include yourself:
    #SPOTIPY_CLIENT_ID='YOUR_CLIENT_ID'
    #SPOTIPY_CLIENT_SECRET='YOUR_CLIENT_SECRET'
    #SPOTIPY_REDIRECT_URI='YOUR_ADDED_REDIRECT_URI' #Example: http://127.0.0.1:9090

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

def sort_spotify_by_language(tracks_with_languages):
    return tracks_with_languages