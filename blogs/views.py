from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic import ListView, DetailView

# Helper functions
def get_date(post):
    return post['date']

# Create your views here.

class StartingPageView(ListView):
    template_name = "blogs/index.html"
    model = Post
    ordering = ['-date']
    context_object_name = 'posts'


    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data

class AllPostView(ListView):
    template_name = 'blogs/all-posts.html'
    model = Post
    ordering = ['-date']
    context_object_name = 'all_posts'


class DetailPostView(DetailView):
    template_name = 'blogs/post-detail.html'
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = self.object.tags.all()  # type: ignore # Get related tags
        return context 

