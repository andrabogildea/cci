from collections import deque
from copy import copy


class Song:
    #this needs to be a singleton
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration
        self.playing = False
        self.curr_sec = 0

    def play(self):
        curr_duration = self.duration - self.curr_sec
        self.playing = True
        while curr_duration > 0 and self.playing:
            time.sleep(1)
            curr_duration -= 1
        self.playing = False
        self.curr_sec = self.duration - curr_duration

    def stop(self):
        self.playing = False


def Playlist:
    def __init__(self):
        self.playlist = deque([])
        self.playing = False

    def start(self):
        if self.playing:
            return
        self.playing = True
        while len(self.playlist) > 0:
            song = self.playlist.popleft()
            while self.playing:
                song.play()
                sleep(1)
                song.stop()

    def stop(self):
        if not self.playing:
            return
        self.playing = False

    def next(self):
        self.stop()
        self.play()

    def add(self, song):
        self.playlist.append(song)

    def reset(self):
        if self.playing:
            self.playing = False
        self.playlist = deque([])


class SongCollection:
    def __init__(self, songs=None):
        if songs in None:
            self.songs = []
        self.songs = []
        self.size = len(self.songs)

    def add(self, song):
        self.songs.append(song)
        self.size += 1
        return self.size - 1

    def remove(self, id):
        if id < self.size:
            del self.songs[id]
            self.size -= 1

    def getSongCodes(self):
        codes = {}
        for i, s in enumerate(self.songs):
            codes[i] = s
        return codes

    def getSong(self, id):
        if id < self.size:
            return self.songs[id]
        return None


def Jukebox:
    def __init__(self, songcolletion, playlist):
        self.songcollection = songcolletion
        self.playlist = playlist

    def getAllSongs(self):
        return self.songcollection.getSongCodes():

    def getSong(self, id):
        return self.songcollectio.getSong(id)

    def add(self, song):
        return self.songcollectio.add(song)

    def remove(self, int):
        self.songcollection.remove(int)

    def reset(self):
        self.playlist.reset()

    def play(self, int):
        song = self.getSong(int)
        if song is not None:
            self.playlist.add(int)

    def start(self):
        self.playlist.start()

    def stop(self):
        self.playlist.stop()
