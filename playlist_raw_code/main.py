from concurrent.futures import thread
from Playlist import Playlist
import threading
path = "C:\\Users\\sahil\\Music\\playlist"
if __name__ == '__main__':
    obj = Playlist() 
    obj.add(path, "que_pena.mp3")
    obj.add(path, "brown_munde.mp3")
    obj.add(path, "tutu.mp3")
    t = threading.Thread(target=obj.play_all)
    t.start()
    obj.next_track()

    