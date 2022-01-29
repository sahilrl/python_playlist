from django.conf import settings

from django.conf import settings

from django.conf import settings

def handle_uploaded_file(title, f):
    print(settings.MEDIA_ROOT)
    path = str(settings.MEDIA_ROOT) + '\\all_songs\\' + title
    with open(path, 'wb') as destination:
        for chunk in f.chunks():
            destination.write(chunk)