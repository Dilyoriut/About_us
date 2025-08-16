from django.http import HttpResponse
from django.shortcuts import render
from .models import Post

# Create your views here.
def blog_list(request):
    posts = Post.objects.all()
    post_list = ""
    for post in posts:
        post_list += f"<li>{post}</li>"
    return HttpResponse(f"<ul>{post_list}</ul>")
