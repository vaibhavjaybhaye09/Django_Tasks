from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoForm
from django.core.paginator import Paginator

# Create your views here.

def todo_list(request):
    todos = Todo.objects.all()
    paginator = Paginator(todos, 3)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)
    context = {
        'page_obj': page_obj
    }
    return render(request, 'crud/todo_list.html', context)

def todo_create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST, request.FILES)
        if form.is_valid():    # ✅ add parentheses
            form.save()
            return redirect('todo_list')  # ✅ use URL name
    else:
        form = TodoForm()
    return render(request, 'crud/todo_create.html', {'form': form})

def todo_update(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        form = TodoForm(request.POST, request.FILES, instance=todo)  # ✅ use instance=todo
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'crud/todo_update.html', {'form': form})  # ✅ fix typo 'foms' → 'form'

def todo_delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.delete()
    return redirect('todo_list')
