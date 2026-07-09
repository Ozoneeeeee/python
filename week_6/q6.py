import random


class Playlist:

    def __init__(self):
        self.songs = []


    def add_song(self, title, artist):
        song = {
            "title": title,
            "artist": artist
        }

        self.songs.append(song)


    def shuffle(self):
        random.shuffle(self.songs)



playlist = Playlist()

playlist.add_song("Shape of You", "Ed Sheeran")
playlist.add_song("Believer", "Imagine Dragons")
playlist.add_song("Perfect", "Ed Sheeran")
playlist.add_song("Faded", "Alan Walker")
playlist.add_song("Counting Stars", "OneRepublic")


playlist.shuffle()


for song in playlist.songs:
    print(song["title"], "-", song["artist"])