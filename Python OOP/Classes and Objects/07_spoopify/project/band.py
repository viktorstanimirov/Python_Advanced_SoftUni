from project.album import Album
from project.song import Song


class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums = []

    def add_album(self, album: Album) -> str:
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."

        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str) -> str:
        for some_album in self.albums:
            if some_album.name == album_name:

                if not some_album.published:
                    self.albums.remove(some_album)
                    return f"Album {some_album.name} has been removed."

                return f"Album has been published. It cannot be removed."

        return f"Album {album_name} is not found."
    def details(self) -> str:
        result = f"Band {self.name}\n"
        for a in self.albums:
            result += f"{a.details()}\n"

        return result[:-1]


