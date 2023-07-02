from django import forms
from .models import images

class ImageForm(forms.ModelForm):
    class Meta:
        model = images
        fields = ('events','image','date_time')