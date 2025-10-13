from django.shortcuts import render,redirect, get_object_or_404
from .models import *
from .forms import StudentForm

# Create your views here.

def stu_list(request):
    students = Student.objects.all()
    return render(request, 'student/stu_list.html', {'students':students})

def stu_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('stu_list')
    else:
        form = StudentForm()  # For GET request (empty form)

    return render(request, 'student/stu_create.html', {'form': form})


def stu_update(request,pk):
    student = get_object_or_404(Student,pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST ,instance=student)
        form.save()
        return redirect('stu_list')
    else: 
        form = StudentForm(instance=student)
    return render(request, 'student/stu_update.html',{'form':form})

def Stu_del(request,pk):
    students = get_object_or_404(Student,pk=pk)
    students.delete()
    return redirect('stu_list') 