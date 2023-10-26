# from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('natural', include('natural.urls')),
]
