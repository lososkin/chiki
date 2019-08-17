from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
	path('addlike/<int:id_devki>/', views.addlike,name='addlike'),
	path('top/', views.top,name='top'),
	path('get2devki/', views.get2devki,name='get2devki'),
	path('vote/<int:id_devki>/', views.vote_devka,name='vote_devka'),
	# path('vote_and_get/<int:id_devki>/', views.vote_and_get,name='vote_and_get'),
    path('', views.poll,name='poll'),
]
