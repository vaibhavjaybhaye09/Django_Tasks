from django.shortcuts import render,get_object_or_404,redirect
from .models import Car,Rental
from .forms import *
from django.contrib import messages

def home(request):
    return render(request,'rent/home.html')


# Create your views here.
def view_available_cars(request):
    cars = Car.objects.filter(is_available = True)
    return render(request,'rent/available_cars.html',{'cars':cars})

def rent_car(request):
    if request.method == 'POST':
      form = RentCarForm(request.POST, request.FILES)
      if form.is_valid():
          username = form.cleaned_data['username'].lower().strip()       
          car_id = form.cleaned_data['car_id']
          days = form.cleaned_data['days']

          car = get_object_or_404(Car,id = car_id, is_available = True)

          total_cost = days * car.price_per_d
          Rental.objects.create(
              username=username,
              car = car,
              days = days,
              total_cost = total_cost
          )
          car.is_available = False
          car.save()

          messages.success(request, f"you rented {car.model} for {days} days. ${total_cost:.2f}")
          return redirect('view_available_cars')
    else:
        form =RentCarForm()
    
    return render(request, 'rent/rent_car.html', {'form':form})

def view_rented_cars(request):
    rented_cars = Rental.objects.filter(returned = False)
    return render(request, 'rent/rented_cars.html', {'rented_cars': rented_cars})

def return_car(request):
    if request.method == 'POST':
        form = ReturnCarForm(request.POST, request.FILES)
        if form.is_valid():
            username = form.clean_data['username'].lower().strip()
            rental = Rental.objects.filter(username= username, returned = False).first()

            if rental:
                rental.returned = True
                rental.save()

                rental.car.is_available = True
                rental.car.save()

                messages.success(request, f"{rental.car.model} has been returned successfuly!")
                return redirect('view_available_cars')
            else:
                messages.error(request, "No active rental found for this user. ")
        
        else: 
            form = ReturnCarForm()

        return render(request, 'rent/return_car.html',{'form':form})

def view_rental_history(request):
    if request.method == 'POST':
        form = RentalHistoryForm(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data['username'].lower().strip()
            history = Rental.objects.filter(username=username)
            return render(request, 'rent/rental_history.html', {'history': history})
    else:
        form = RentalHistoryForm()

    # Always return a response
    return render(request, 'rent/rental_history.html', {'form': form})