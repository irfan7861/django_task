from django.contrib import admin 
from django.urls import path 

# importing views from views..py 
from .views import app_view 

urlpatterns = [ 
	path('', app_view ), 
] 