from django import forms
from .models import Booking


class FlightSearchForm(forms.Form):
    departure_city = forms.CharField(max_length=100)
    arrival_city = forms.CharField(max_length=100)


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['full_name', 'email']
