from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    required_css_class='required_field'
    class Meta:
        model=Movie
        fields=['name','desc','year','image']

