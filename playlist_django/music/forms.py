from django import forms

class UploadMusic(forms.Form):
    title = forms.CharField(max_length=250)
    file = forms.FileField(required=False)