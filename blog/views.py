from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.
class HomeListView(ListView):
    model=Post
    template_name='index.html'
    
class HomeDetailView(DetailView):
    model = Post
    template_name = 'post-detail.html'