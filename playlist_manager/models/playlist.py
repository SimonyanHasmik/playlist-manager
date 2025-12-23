class Playlist:
    def __init__(self, name):
        self.name = name
        self._songs = []

    @property
    def songs(self):
        return self._songs

    def add_song(self, song):
        self._songs.append(song)

    def __len__(self):
        return len(self._songs)

    def __repr__(self):
        return f"<Playlist {self.name} ({len(self)} songs)>"
