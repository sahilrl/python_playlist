from .linked_list import Composition, LinkedList
# from pygame import mixer
# from mutagen.mp3 import MP3
import json


class Playlist(LinkedList):
    def __init__(self, name = 'New Playlist'):
        super().__init__()
        self.playing = None
        self.name = name
    
    def add(self, path, name):
        self.append_right(Composition(path, name))

    @property
    def current(self):
        if self.playing is None:
            self.playing = self.head.next_item
        return self.playing
    
    @current.setter
    def current(self, song):
        self.playing = song

    # this function is where the music is actually played 
    # using pygame.mixer lib
    # def play(self, song):
    #     self.current = song
    #     song = str(self.current.data)
    #     song_len = MP3(song)
    #     song_len = song_len.info.length
    #     mixer.init()
    #     sound = mixer.Sound(song)
    #     sound.play()
    #     time.sleep(song_len)

    def play_all(self):
        lis = []
        current = self.head
        while True:
            current = current.next_item
            if current.data != None:
                self.play(self, current)

        
    def next_track(self):
        self.current = self.current.next_item
        return self.current.data
    

    def prev_track(self):
        self.current = self.current.prev_item
        return self.current.data
        

