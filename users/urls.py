from django.contrib import admin 
from django.urls import path 
from django.conf.urls import include
from .views import register

app_name = 'users'

urlpatterns = [
	path("register", register, name="register"),
	path( "", include("django.contrib.auth.urls")),
]