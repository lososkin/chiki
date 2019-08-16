from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
	path('top/', views.top,name='top'),
    path('', views.poll,name='poll'),
]
