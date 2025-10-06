from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib import messages
from django.contrib.auth import login
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView, DeleteView,DetailView,UpdateView,CreateView

def home(request):
    blogs = Blog.objects.filter(is_published = True)
    categories = Category.objects.all()
    search_query = request.GET.get('search')
    print(search_query)
    if search_query:
        blogs = blogs.filter(
            Q(title_icontains=search_query) |
            Q(content_icotains=search_query) |
            Q(author__username__icontains=search_query)
        )

    category_filter= request.GET.get('search')
    print(category_filter)
    if category_filter:
        blogs = blogs.filter(
            categories__id = category_filter

        )

    paginator = Paginator(blogs,5)
    page_number = request = request.GET('page')
    page_obj = paginator.get_page(page_number)


    context ={
        'page_obj': page_obj,
        'categorise' : categories,
        'search_query': search_query,
        'selected_category':category_filter
    }
    return render(request, 'home.html', context)

class BlogDetailView(DetailView):
    model = Blog
    template_name= 'blog/detail.html'
    context_object_name = 'blog'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blog = self.get_object()
        blog.views  +=1
        blog.save()

        context['comment'] = blog.comments.filter(parent = None)
        context['comment_form'] = CommentForm()
        if self.request.user.is_authenticated:
            context['user_liked'] = Bloglike.objects.filter(
                user = self.request.user,
                blog = blog
            ).exists()
            
            context['like_cont'] = blog.likes.count()
            return context



class BlogCreateView(LoginRequiredMixin,CreateView):
    model = Blog
    form_class = BlogsForm
    template_name ='blog/create.hmtl'
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valis(form)
    


class BlogUpdateView(LoginRequiredMixin,UpdateView):
    model=Blog
    form_class = BlogsForm
    template_name = 'blog/edit.html'
    def test_func(self):
        blog = self.get_object()
        return self.request.user == blog.author



def register(request):
    if request.method == 'POST':
        form = CustomUserCreationFrom(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            return redirect('/')
    
    else :
        form = CustomUserCreationFrom()
    return render(request, 'account/registe.html',{'form':form})


