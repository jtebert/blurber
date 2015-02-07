from django import forms
from models import *

class SaveBlurb(forms.ModelForm):
    class Meta:
        model = Blurb
        fields = ('title', 'author', 'descr', 'genre_str')
        widgets = {
            'title': forms.HiddenInput,
            'author': forms.HiddenInput,
            'descr': forms.HiddenInput,
            'genre_str': forms.HiddenInput,
        }