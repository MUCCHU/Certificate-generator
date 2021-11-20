from django.contrib import admin
from django.urls import path
from app import views
urlpatterns = [
    path('', views.index, name='index'),
    path('certi/', views.certi, name='certi'),
    path('pilcerti/', views.PILcerti, name='pilcerti'),

 ]