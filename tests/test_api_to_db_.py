from playlist_manager.api.manager import PlaylistManager

manager = PlaylistManager()

# Ստուգել playlist-ները
playlists = manager.get_playlists()
print("Playlists:", playlists)

# Ստուգել առաջին playlist-ի երգերը
if playlists:
    songs = manager.get_songs(playlists[0][0])
    print("Songs in first playlist:", songs)
