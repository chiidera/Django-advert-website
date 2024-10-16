from django import forms
from .models import Advert


class AdvertForm(forms.ModelForm):
    class Meta:
        model  = Advert
        fields = ['title', 'description', 'link', 'image']