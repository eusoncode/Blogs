from django.shortcuts import render

# Create your views here.

def starting_page(request):
    return render(request, "blogs/index.html")

def posts():
    pass

def post_detail():
    pass
