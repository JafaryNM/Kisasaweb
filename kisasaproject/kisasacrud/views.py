from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView,UpdateView, CreateView
from .models import Core
from .forms import PostForm
from django.urls import reverse_lazy

# Create your views here.
class IndexTemplate(ListView):

    template_name='test.html'
    model=Core

class SingleView(DetailView):

    template_name='single.html'
    model=Core
    context_object_name='post'

class PostView(ListView):

    template_name='post.html'
    model=Core
    context_object_name='post_list'

class AddPost(CreateView):
    model=Core
    template_name='addpost.html'
    form_class= PostForm
    success_url= reverse_lazy('post')
