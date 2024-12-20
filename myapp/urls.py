from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello),
    path('', views.renderHtml, name='home'),
    path('posts/', views.renderPosts, name='posts'),
    path('add/', views.add_post, name='add_post'),
]