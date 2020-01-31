from django.contrib import admin
from django.urls import path,include

from . import views
urlpatterns = [
	path('', views.home,name='home'),
	path('forms/', views.form_entry,name='form'),
	path('profile/<person_id>', views.profile,name='profile'),
	path('search/',views.search,name='search'),
	path('title_search/', views.title_search, name='title_search')

]