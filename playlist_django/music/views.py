from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .backend import Playlist
from django.conf import settings
path = "C:\\Users\\sahil\\Music\\playlist"

obj = Playlist.Playlist()

def home(request):
    song_name = ''
    return render(request, 'music/index.html', {'song_name': song_name})


def play(request):
    song = obj.display()
    print(f'this is song...........{song}')
    return HttpResponse(song)
