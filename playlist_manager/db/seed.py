# playlist_manager/db/seed.py
import requests
from multiprocessing import Process
from threading import Thread
from playlist_manager.api.manager import PlaylistManager
from playlist_manager.models.song import Song

# Fetch songs from API (I/O-bound)
def fetch_songs_from_api(term="pop", limit=20):
    url = "https://itunes.apple.com/search"
    params = {"term": term, "limit": limit, "media": "music"}
    response = requests.get(url, params=params)
    data = response.json()
    songs = []
    for item in data.get("results", []):
        song = Song(
            title=item.get("trackName", "Unknown"),
            artist=item.get("artistName", "Unknown"),
            duration=int(item.get("trackTimeMillis", 0) // 1000),  # վայրկյան
            genre=item.get("primaryGenreName", "Unknown")
        )
        songs.append(song)
    return songs

# Insert songs into DB (I/O-bound)
def insert_songs(songs):
    manager = PlaylistManager()
    manager.create_playlist("API Playlist")
    playlist_id = manager.get_last_playlist_id()  # ստանում ենք վերջնական playlist id

    for song in songs:
        manager.add_song(playlist_id, song)

    # Print inserted data
    print("Inserted playlist and songs:")
    playlists = manager.get_playlists()
    for pl in playlists:
        print("Playlist:", pl)
        songs_in_pl = manager.get_songs(pl[0])
        for s in songs_in_pl:
            print(" -", s)

# Combine multiprocessing + threading
def process_api_data():
    songs = fetch_songs_from_api("pop", 20)  # I/O-bound
    t = Thread(target=insert_songs, args=(songs,))
    t.start()
    t.join()

def run_seed():
    p = Process(target=process_api_data)  # CPU-bound wrapper
    p.start()
    p.join()

if __name__ == "__main__":
    run_seed()
