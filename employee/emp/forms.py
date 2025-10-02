from django import forms
from .models import Employee, Position


class PositionForm(forms.models.ModelForm):
    class Meta:
        model = Position
        fields =['title']



class EmployeeForm(forms.models.ModelForm):
    class Meta:
        model = Employee
        fields = ['full_name','emp_code', 'mobile', 'position']
        