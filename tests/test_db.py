from playlist_manager.api.manager import PlaylistManager

manager = PlaylistManager()
playlist_id = manager.get_last_playlist_id()
songs = manager.get_songs(playlist_id)
print("Songs in playlist:", songs)
