from django.shortcuts import render,redirect,get_object_or_404
from .models import Gallary
from .forms import GallaryForm


# Create your views here.
def gall_l(request):
    photos = Gallary.objects.all()
    return render(request, 'gallary/gall_l.html', {'photos':photos})


def gall_c(request):
    if request.method == 'POST':
        form = GallaryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gall_l')
    else:
        form = GallaryForm()
    return render(request, 'gallary/gall_c.html',{'form':form})

def update(request,pk):
    photos = get_object_or_404(Gallary,pk=pk)
    if request.method == 'POST':
        form = GallaryForm(request.POST,request.FILES, instance=photos)
        if form.is_valid():
            form.save()
            return redirect('gall_l')
    else:
        form = GallaryForm(instance=photos)

    return render(request, 'gallary/update.html',{'form':form})


def delete(request,pk):
    photo = get_object_or_404(Gallary,pk=pk)
    photo.delete()
    return redirect('gall_l')
    