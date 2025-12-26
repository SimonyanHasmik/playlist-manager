# Playlist Manager

## Project Overview
Playlist Manager is a Python package designed to manage music playlists efficiently. It allows users to create playlists, add or remove songs, and fetch music data from public APIs such as iTunes. The package demonstrates proper Python practices including the use of multiple interrelated classes, encapsulation, properties, and dunder methods like `__repr__`, `__eq__`, and `__len__`. Data persistence is implemented via SQLite, and concurrency is utilized to efficiently handle CPU-bound and I/O-bound tasks. This project is ideal for learning advanced Python concepts while creating a functional application.

## Project Structure│
```text
playlist-manager/
├── playlist_manager/
│   ├── __init__.py
│   ├── api/
│   │   ├── __init__.py
│   │   └── manager.py
│   ├── db/
│   │   ├── __init__.py
│   │   ├── database.py
│   │   └── seed.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── song.py
│   └── utils/
│       ├── __init__.py
│       └── decorators.py
├── tests/
│   ├── test_api_to_db_.py
│   └── test_db.py
├── README.md
├── pyproject.toml
├── setup.py
└── requirements.txt

```

## Installation

1. **Create a virtual environment** (optional but recommended):

```powershell
python -m venv venv
.\venv\Scripts\activate
```
## 🔗 TestPyPI Link

You can find the published package on **TestPyPI** at the following link:

https://test.pypi.org/project/playlist-manager/0.1.1/

---

Database Initialization

Create the database and tables:

python -m playlist_manager.db.database


Seed the database with initial data (uses multiprocessing + multithreading):

python -m playlist_manager.db.seed


The database file playlists.db will be created in the db/ folder.


## 📦 API Implementation (manager.py)

This section describes the **actual API implementation** used in the project.  
The file is located at:


The **`PlaylistManager`** class acts as the main API layer.  
Users interact only with this class — all database logic is encapsulated internally.

---

## 🧠 API Design Overview

- Uses **SQLite** through the `Database` class
- Applies **encapsulation**: database access is hidden from the user
- Uses **composition**: `PlaylistManager` owns a `Database` instance
- Uses a custom decorator `@log_action` for logging API operations
- Works with domain objects such as `Song`

---

## 🧩 PlaylistManager API Code

```python
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

        # Check if playlist already exists
        cur.execute("SELECT id FROM playlists WHERE name=?", (name,))
        result = cur.fetchone()

        if result:
            print(f"Playlist '{name}' already exists.")
            return result[0]

        # Create new playlist
        cur.execute("INSERT INTO playlists(name) VALUES (?)", (name,))
        self.db.conn.commit()
        print(f"Playlist '{name}' created.")
        return cur.lastrowid

    @log_action
    def get_playlists(self):
        cur = self.db.conn.cursor()
        cur.execute("SELECT id, name FROM playlists")
        return cur.fetchall()

    @log_action
    def delete_playlist(self, playlist_id: int):
        cur = self.db.conn.cursor()

        # Delete songs belonging to the playlist
        cur.execute("DELETE FROM songs WHERE playlist_id=?", (playlist_id,))
        cur.execute("DELETE FROM playlists WHERE id=?", (playlist_id,))
        self.db.conn.commit()

    # Song Methods
    def add_song(self, playlist_id: int, song: Song):
        cur = self.db.conn.cursor()
        cur.execute(
            """
            INSERT INTO songs (playlist_id, title, artist, duration, genre)
            VALUES (?, ?, ?, ?, ?)
            """,
            (playlist_id, song.title, song.artist, song.duration, song.genre),
        )
        self.db.conn.commit()

    @log_action
    def get_songs(self, playlist_id: int):
        cur = self.db.conn.cursor()
        cur.execute(
            """
            SELECT id, title, artist, duration, genre
            FROM songs
            WHERE playlist_id=?
            """,
            (playlist_id,),
        )
        return cur.fetchall()

    @log_action
    def delete_song(self, song_id: int):
        cur = self.db.conn.cursor()
        cur.execute("DELETE FROM songs WHERE id=?", (song_id,))
        self.db.conn.commit()

    # Utility
    def get_last_playlist_id(self):
        cur = self.db.conn.cursor()
        cur.execute("SELECT id FROM playlists ORDER BY id DESC LIMIT 1")
        result = cur.fetchone()
        return result[0] if result else None
```
## ⚙️ Concurrency

Concurrency is applied thoughtfully to improve performance where it truly matters:

- **Multiprocessing**
  - Implemented in `seed.py`
  - Used for **CPU-bound tasks**, such as processing large datasets
  - Enables parallel execution across multiple CPU cores

- **Multithreading**
  - Implemented in `seed.py`
  - Used for **I/O-bound tasks**, such as inserting large numbers of songs into the database
  - Improves throughput while waiting for disk I/O operations

Each concurrency technique is chosen with a **clear and justified purpose**, ensuring efficient and scalable performance.

---

## ✨ Features

- Modular **Python package structure** with reusable components
- **Object-Oriented Design** using composition and encapsulation
- At least **three interconnected classes**:
  - `PlaylistManager`
  - `Song`
  - `Database`
- Implementation of Python **dunder methods**:
  - `__repr__`
  - `__eq__`
  - `__len__`
- **SQLite-based** persistent data storage
- Clean **API layer** for full CRUD (Create, Read, Update, Delete) operations
- Built-in **concurrency support** for handling large datasets efficiently
- Fully prepared for publishing on **PyPI** or **TestPyPI**

