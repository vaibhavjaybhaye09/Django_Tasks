from django import forms
from .models import Gallary

class GallaryForm(forms.ModelForm):
 class Meta:
    model = Gallary
    fields = ['title','image']


    