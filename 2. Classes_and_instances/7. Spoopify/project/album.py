class Album:

    def __init__(self, name, *args):
        self.name = name
        self.songs = [song for song in args]
        self.published = False

    def add_song(self, song):
        if self.published:
            return f'Cannot add songs. Album is published.'
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        if song not in self.songs:
            self.songs.append(song)
            return f"Song {song.name} has been added to the album {self.name}."
        else:
            return f"Song is already in the album."

    def remove_song(self, song_name):
        if self.published:
            return f"Cannot remove songs. Album is published."
        for song in self.songs:
            if song_name == song.name:
                self.songs.remove(song)
                return f"Removed song {song.name} from album {self.name}."
        return f"Song is not in the album."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        result = f"Album {self.name}\n"
        for song in self.songs:
            result += f"== {song.get_info()}\n"
        return result
