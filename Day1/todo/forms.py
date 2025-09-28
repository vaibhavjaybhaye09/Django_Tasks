from django import forms
from .models import Todo

class TodoForm(forms.models.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'completed']