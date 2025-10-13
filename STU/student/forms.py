from django import forms
from .models import Student

class StudentForm(forms.models.ModelForm):
    class Meta:
        model = Student
        fields = ['name','email','course',]