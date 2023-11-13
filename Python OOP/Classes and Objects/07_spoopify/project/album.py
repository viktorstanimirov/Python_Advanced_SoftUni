from project.song import Song


class Album:
    def __init__(self, name: str, *songs: str) -> None:
        self.name = name
        self.published = False
        self.songs = [*songs]

    def add_song(self, song) -> str:
        if song in self.songs:
            return "Song is already in the album."
        if self.published:
            return "Cannot add songs. Album is published."
        if song.single:
            return f"Cannot add {Song.__name__}. It's a single"

        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        if self.published:
            return f"Cannot remove songs. Album is published."

        for some_song in self.songs:
            if some_song.name == song_name:
                self.songs.remove(some_song)

                return f"Removed song {song_name} from album {self.name}."

        return f"Song is not in the album."

    def publish(self) -> str:
        if self.published:
            return f"Album {self.name} is already published."

        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        result = f"Album {self.name}\n"
        for s in self.songs:
            result += f"== {s.get_info()}\n"

        return result[:-1]
