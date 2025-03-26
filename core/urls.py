from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('/about', views.about, name='about'),
    path('/contacts', views.contacts, name='contacts'),
]
