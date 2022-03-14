from django.urls import path
from . import views

urlpatterns = [
    path('smartcamera/', views.smartcamera, name='smartcamera')
] 