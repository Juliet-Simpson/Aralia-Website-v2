from django.urls import path
from . import views

urlpatterns = [
    path('assetlink.json', views.digital_assets, name='assetslink')
]