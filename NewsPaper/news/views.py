from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

class PostList(ListView):
    model = Post
    ordering = ['-creationData']
    template_name = 'post/posts.html'
    context_object_name = 'posts'


class PostDetail(DetailView):
    model = Post
    template_name = 'post/post.html'
    context_object_name = 'post'
    queryset = Post.objects.all()