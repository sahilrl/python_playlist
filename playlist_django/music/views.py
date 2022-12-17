from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from .backend import Playlist
from .forms import UploadMusic
from .tools import handle_uploaded_file
from django.conf import settings

obj = Playlist.Playlist()

def home(request):
    return render(request, 'music/index.html')


def play(request):
    return 

def makePlaylist(request):
    
    return




