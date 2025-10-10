from django.shortcuts import render, redirect, get_object_or_404
from .models import Event
from .forms import EventForm
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator

# Home - List all Events
def home(request):
    events = Event.objects.all()
    return render(request, 'evnt/home.html', {'events': events})

# Create Event
def e_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Event Created Successfully!")
            return redirect('home')   # Redirect after save
    else:
        form = EventForm()
    return render(request, 'evnt/e_create.html', {'form': form})

# Update Event
def e_update(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, "Event Updated Successfully!")
            return redirect('home')
    else:
        form = EventForm(instance=event)
    return render(request, 'evnt/e_update.html', {'form': form})

# Delete Event
def e_delete(request, pk):
    event = get_object_or_404(Event, pk=pk)
    event.delete()
    messages.success(request, "Event Deleted Successfully!")
    return redirect('home')
