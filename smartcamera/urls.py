from django.urls import path
from . import views

urlpatterns = [
    path('', views.smartcamera, name='smartcamera')
] 