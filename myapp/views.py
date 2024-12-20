from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import BlogPost
from .forms import BlogPostForm

def renderHtml(req):
    return render(req, 'myapp/home.html')

def hello(req):
    return HttpResponse("Hello")

def renderPosts(req):
    posts = BlogPost.objects.all()
    return render(req, 'myapp/posts.html', {'posts': posts})

def add_post(req):
    if req.method == 'POST':
        form = BlogPostForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('posts')
    else:
        form = BlogPostForm()

    return render(req, 'myapp/add_post.html', {'form': form})

