from django.urls import path
from . import views

urlpatterns = [
    path('assetslink.json', views.digital_assets, name='assetslink')
]