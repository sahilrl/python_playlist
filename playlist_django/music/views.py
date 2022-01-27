from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .backend import Playlist
path = "C:\\Users\\sahil\\Music\\playlist"

obj = Playlist.Playlist()

def home(request):
    obj.add(path, "bro.mp3")
    obj.add(path, "aue.mp3")
    return render(request, 'music/index.html')


def play(request):
    song = obj.display()
    print(f'this is song...........{song}')
    return HttpResponse(song)
