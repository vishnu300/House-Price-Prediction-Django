from django.contrib import admin
from django.urls import path
from .views import home,price
urlpatterns = [
    path('homeprice/', home),
    
    path('homeprice/result', price)
]
