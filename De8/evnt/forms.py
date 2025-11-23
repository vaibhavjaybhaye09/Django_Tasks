from django import forms
from .models import Event

class EventForm(forms.models.ModelForm):
    class Meta:
        model = Event
        feilds =['title', 'location', 'picture','date']