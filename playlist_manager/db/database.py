import sqlite3
import os

DB_FILE = os.path.join(os.path.dirname(__file__), "playlists.db")


class Database:
    def __init__(self, db_name=DB_FILE):
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS playlists (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE
        )
        """)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS songs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            playlist_id INTEGER,
            title TEXT,
            artist TEXT,
            duration INTEGER,
            genre TEXT,
            FOREIGN KEY (playlist_id) REFERENCES playlists(id)
        )
        """)
        self.conn.commit()


if __name__ == "__main__":
    db = Database()
    print(f"Database created at {DB_FILE}")  # <-- այս տողը
