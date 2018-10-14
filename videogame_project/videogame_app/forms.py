from django import forms
from .models import GameIdea

class gameentry(forms.ModelForm):
    class Meta:
        model= GameIdea
        fields ={'name', 'genre'}