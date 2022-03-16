from django.urls import path
from . import views

urlpatterns = [
    path('', views.surfacescanner, name='surfacescanner')
] 