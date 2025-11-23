from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import Todo
from .forms import TodoForm


# Create your views here.


class TodoListVIew(ListView):
    model = Todo
    template_name ='todo/todo_list.html'
    context_object_name = 'todos'
  

class TodoCreateView(CreateView):
    model =Todo
    form_class = TodoForm
    template_name ='todo/todo_create.html'
    success_url = reverse_lazy('todo_list')

class TodoDeleteView(DeleteView):
    model = Todo
    template_name = 'todo/todo_del_cnf.html'
    success_url = reverse_lazy('todo_list')


class TodoUpdateView(UpdateView):
    model = Todo
    form_class = TodoForm
    template_name ='todo/todo_update.html'
    success_url = reverse_lazy('todo_list')