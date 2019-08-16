from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
	path('addlike/<int:id_devki>/', views.addlike,name='addlike'),
	path('top/', views.top,name='top'),
    path('', views.poll,name='poll'),
]
