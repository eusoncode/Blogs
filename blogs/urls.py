from django.urls import path
from . import views

urlpatterns = [
    path("", views.StartingPageView.as_view(), name="starting-page"),
    path("posts", views.AllPostView.as_view(), name="posts-page"),
    path("post/<slug:slug>", views.DetailPostView.as_view(), name="post-detail-page"),   #/posts/my-first-post
    path("read-later/<slug:slug>", views.ReadLaterView.as_view(), name="read-later")
]