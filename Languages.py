from langdetect import detect
import iso639

def get_lyrics_language(tracks_with_lyrics):
    '''
    Because the english language is in the majority among my playlists, it
    will be harder to sort foreign languages in the english playlist.
    Therefore, the priority will be given to the detection of non-english text,
    either by the lyrics, song name or album. The selection priority will be
    lyrics > song name > album.
    '''
    tracks_with_languages = []
    for track in tracks_with_lyrics:
        artists = track[0]
        song_name = track[1]
        album = track[2]
        song_uri = track[3]
        try: lyrics = track[4]
        except: lyrics = 'unknown'

        #Language detection
        print('Checking language of {} from {}.'.format(artists, song_name))
        try: song_name_lang = detect(song_name)
        except: song_name_lang = 'unknown'
        try: album_lang = detect(album)
        except: album_lang = 'unknown'

        lyrics_lang = detect(lyrics)

        if lyrics_lang == song_name_lang == album_lang:
            language = lyrics_lang
        else:
            if lyrics_lang != 'en' and lyrics_lang != 'unknown':
                language = lyrics_lang
            elif song_name_lang != 'en' and song_name_lang != 'unknown':
                language = song_name_lang
            elif album_lang != 'en' and album_lang != 'unknown':
                language = album_lang
            else:
                language = lyrics_lang

        #Language selection
        try:
            native = iso639.to_native(language).split(';')[0] #Converts to native
            english = iso639.to_name(language).split(';')[0] #Converts to english
            if native != english:
                language = '{} ({})'.format(native, english)
            else: #Invalid code
                language = native
        except:
            pass
        print('Language: ' + language)
        tracks_with_languages.append([song_uri, language])

    tracks_with_languages = sorted(tracks_with_languages, key=lambda x: x[1]) #Sorting by language
    return tracks_with_languages