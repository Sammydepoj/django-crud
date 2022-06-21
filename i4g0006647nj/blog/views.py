from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy

from .models import Post

class PostListView (ListView):
    models=Post
    template_name = 'post_list.html'
    success_url  = reverse_lazy("blog:all")


class PostCreateView (CreateView):
    model = Post
    fields = "__all__"

    template_name = 'post_form.html'
    success_url  = reverse_lazy("blog:all")

class PostDetailView(DetailView):
    model=Post
    template_name = 'post_detail.html'


class PostUpdateView(UpdateView):
    model=Post
    fields = "__all__"
    template_name = 'post_detail.html'
    success_url  = reverse_lazy("blog:all")  


class PostDeleteView(DeleteView):
     model=Post
     fields = "__all__"
     template_name = 'post_confirm_delete.html'
     success_url  = reverse_lazy("blog:all")
     
# Create your views here.
