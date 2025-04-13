from django.shortcuts import render
from .models import Flight
from .forms import FlightSearchForm
from .forms import BookingForm

def search_flights(request):
    form = FlightSearchForm(request.GET or None)
    flights = None
    if form.is_valid():
        flights = Flight.objects.filter(
            departure_city__icontains=form.cleaned_data['departure_city'],
            arrival_city__icontains=form.cleaned_data['arrival_city']
        )
    return render(request, 'flights/search.html', {'form': form, 'flights': flights})



def book_flight(request, flight_id):
    flight = Flight.objects.get(pk=flight_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.flight = flight
            booking.save()
            return render(request, 'flights/confirmation.html', {'booking': booking})
    else:
        form = BookingForm()
    return render(request, 'flights/book.html', {'form': form, 'flight': flight})