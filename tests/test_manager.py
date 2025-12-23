from playlist_manager.api.manager import PlaylistManager
from playlist_manager.models.song import Song

manager = PlaylistManager()

# 1. Ստեղծել նոր playlist
manager.create_playlist("My Test Playlist")

# 2. Ավելացնել երգ
song = Song("Shape of You", "Ed Sheeran", 233, "Pop")
playlist_id = manager.get_last_playlist_id()
manager.add_song(playlist_id, song)

# 3. Վերցնել playlist-ները
playlists = manager.get_playlists()
print("Playlists:", playlists)

# 4. Վերցնել երգերը playlist-ում
songs = manager.get_songs(playlist_id)
print("Songs in playlist:", songs)
