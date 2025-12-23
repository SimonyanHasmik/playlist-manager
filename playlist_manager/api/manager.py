from playlist_manager.db.database import Database
from playlist_manager.models.song import Song
from playlist_manager.utils.decorators import log_action
from typing import List, Optional

class PlaylistManager:
    def __init__(self):
        self.db = Database()

    @log_action
    def create_playlist(self, name: str):
       cur = self.db.conn.cursor()
        # Ստուգել, արդյոք արդեն կա playlist
       cur.execute("SELECT id FROM playlists WHERE name=?", (name,))
       result = cur.fetchone()
       if result:
           print(f"Playlist '{name}' արդեն գոյություն ունի։")
           return result[0]  # վերադարձնում ենք playlist-ի ID
       # Եթե չկա, ստեղծել նոր playlist
       cur.execute("INSERT INTO playlists(name) VALUES (?)", (name,))
       self.db.conn.commit()
       print(f"Playlist '{name}' ստեղծվեց։")
       return cur.lastrowid

    @log_action
    def get_playlists(self):
        cur = self.db.conn.cursor()
        cur.execute("SELECT id, name FROM playlists")
        return cur.fetchall()

    @log_action
    def delete_playlist(self, playlist_id: int):
        cur = self.db.conn.cursor()
        # Ջնջել բոլոր երգերը playlist-ից
        cur.execute("DELETE FROM songs WHERE playlist_id=?", (playlist_id,))
        cur.execute("DELETE FROM playlists WHERE id=?", (playlist_id,))
        self.db.conn.commit()

    #Song Methods
    def add_song(self, playlist_id: int, song: Song):
        cur = self.db.conn.cursor()
        cur.execute("""
            INSERT INTO songs (playlist_id, title, artist, duration, genre)
            VALUES (?, ?, ?, ?, ?)
        """, (playlist_id, song.title, song.artist, song.duration, song.genre))
        self.db.conn.commit()

    @log_action
    def get_songs(self, playlist_id: int):
        cur = self.db.conn.cursor()
        cur.execute("""
            SELECT id, title, artist, duration, genre
            FROM songs
            WHERE playlist_id=?
        """, (playlist_id,))
        return cur.fetchall()

    @log_action
    def delete_song(self, song_id: int):
        cur = self.db.conn.cursor()
        cur.execute("DELETE FROM songs WHERE id=?", (song_id,))
        self.db.conn.commit()

    #Utility
    def get_last_playlist_id(self):
        cur = self.db.conn.cursor()
        cur.execute("SELECT id FROM playlists ORDER BY id DESC LIMIT 1")
        result = cur.fetchone()
        return result[0] if result else None
