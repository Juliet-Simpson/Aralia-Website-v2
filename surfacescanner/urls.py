from django.urls import path
from . import views

urlpatterns = [
    path('surfacescanner/', views.surfacescanner, name='surfacescanner')
] 