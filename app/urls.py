from django.contrib import admin
from django.urls import path
from .views import validate

urlpatterns = [
    path('',validate.as_view()),
]
