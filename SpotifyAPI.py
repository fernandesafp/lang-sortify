import spotipy
from spotipy.oauth2 import SpotifyOAuth

def sort_spotify_by_language(tracks_with_languages):
    #Add to environment or include yourself
    scope = 'playlist-modify-private'
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    username = sp.current_user()['display_name']

    prev_lang = tracks_with_languages[0][1]
    new_playlist = sp.user_playlist_create(username, prev_lang, public=False, description='Automated playlist')
    track_arr = []
    for track in tracks_with_languages:
        language = track[1]
        if prev_lang != language:
            sp.user_playlist_add_tracks(username, new_playlist['id'], track_arr)
            new_playlist = sp.user_playlist_create(username, language, public=False, description='Automated playlist')
            track_arr = []
            prev_lang = language

        uri = track[0]
        track_arr.append(uri)

        if len(track_arr) == 100: #Limit of 100 per request
            sp.user_playlist_add_tracks(username, new_playlist['id'], track_arr)
            track_arr = []
    sp.user_playlist_add_tracks(username, new_playlist['id'], track_arr)

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
        track_album = track['track']['album']['name']
        track_uri = track['track']['uri']
        artists_array = []
        for artist in track['track']['artists']:
            artists_array.append(artist['name'])
        track_array.append([artists_array, track_name, track_album, track_uri])
        print('Adding {} from {}'.format(track_name, artists_array))

    return track_array