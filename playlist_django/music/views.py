from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from .backend import Playlist
from .forms import UploadMusic
from .tools import handle_uploaded_file
from django.conf import settings

obj = Playlist.Playlist()

def home(request):
    title = ''
    
    
    return render(request, 'music/index.html', {'title': title})


def add_song(request):
    if request.method == 'POST':
        form = UploadMusic(request.POST, request.FILES)
        if form.is_valid():
            title = request.POST['title']
            path = str(settings.MEDIA_ROOT) + '\\all_songs\\'
            try:
                handle_uploaded_file(title, request.FILES['file'])
            except:
                pass
            obj.add(path, title)
            print(title)
            return redirect(add_song)
        else:
            return HttpResponse(form.errors.as_json())
    else:
        form = UploadMusic()  
    return render(request, 'music/add-music.html', {'form': form})

