from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import CommentForm
from django.views.generic import ListView, View
from django.http import HttpResponseRedirect
from django.urls import reverse

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


class DetailPostView(View):
    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        context = {
            "post": post,
            "tags": post.tags.all(),
            "comment_form": CommentForm(),
            "comments": post.comments.all().order_by("-id") # type: ignore
        }
        return render(request, "blogs/post-detail.html", context)

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()

            return HttpResponseRedirect(reverse("post-detail-page", args=[slug]))
        
        context = {
            "post": post,
            "tags": post.tags.all(),
            "comment_form": comment_form,
            "comments": post.comments.all().order_by("-id") # type: ignore
        }
        return render(request, "blogs/post-detail.html", context)