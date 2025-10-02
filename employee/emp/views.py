from django.shortcuts import render,redirect, get_object_or_404
from .models import Employee, Position
from .forms import EmployeeForm, PositionForm
from django.db.models import Q
from django.core.paginator import Paginator


# Create your views here.
def emp_list(request):
    emplo = Employee.objects.all()
    return render(request, 'emp/emp_list.html', {'emplo':emplo})


def emp_form(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('emp_list')
    else:
        form = EmployeeForm
    return render(request, 'emp/emp_form.html', {'form': form})


def emp_update(request,pk):
    emplo = get_object_or_404(Employee, pk=pk)
    if request.method == "POST":
        form = EmployeeForm(request.POST , request.FILES, instance=emplo)
        if form.is_valid():
            form.save()
            return redirect('emp_list')
    else:
        emplo = EmployeeForm(instance= emplo)
    return render(request, 'emp/emp_update.html' ,{'form':form})

def emp_del(request,pk):
    emplo = get_object_or_404(Employee, pk=pk)
    emplo.delete()
    return redirect('emp_delete')

def position_form(request):
    if request.method == 'POST':
        form = PositionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('emp_list')
    else:
        form = PositionForm
    return render(request, 'emp/position_form.html', {'form': form})

def position_update(request,pk):
    posi = get_object_or_404(Position, pk=pk)
    if request.method == "POST":
        form = PositionForm(request.POST , request.FILES, instance=posi)
        if form.is_valid():
            form.save()
            return redirect('emp_list')
    else:
        form = PositionForm(instance= posi)
    return render(request, 'emp/position_form.html' ,{'form':form})

def position_delete(request,pk):
    posi = get_object_or_404(Position, pk=pk)
    posi.delete()
    return redirect('emp_list')