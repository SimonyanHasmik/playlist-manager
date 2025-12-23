class Song:
    def __init__(self, title, artist, duration, genre):
        self._title = title
        self._artist = artist
        self._duration = duration  # seconds
        self._genre = genre

    #properties
    @property
    def title(self):
        return self._title

    @property
    def artist(self):
        return self._artist

    @property
    def duration(self):
        return self._duration

    @property
    def genre(self):
        return self._genre

    #dunder methods
    def __repr__(self):
        return f"<Song {self.title} by {self.artist}>"

    def __eq__(self, other):
        return (
            isinstance(other, Song)
            and self.title == other.title
            and self.artist == other.artist
        )

    def __len__(self):
        return self.duration
