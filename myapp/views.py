from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import BlogPost
from .forms import BlogPostForm

def renderHtml(req):
    return render(req, 'myapp/home.html')

def hello(req):
    return HttpResponse("Hello")
