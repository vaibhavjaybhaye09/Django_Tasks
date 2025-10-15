from django import forms
from .models import Car,Rental

class RentCarForm(forms.Form):
    username = forms.CharField(max_length=100)
    car_id = forms.IntegerField()
    days = forms.IntegerField(min_value=1)



class ReturnCarForm(forms.Form):
    username = forms.CharField(max_length=100)


class RentalHistoryForm(forms.Form):
    username = forms.CharField(max_length=100)
    