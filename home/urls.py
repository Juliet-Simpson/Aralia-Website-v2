from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('investors/', views.investors, name='investors'),
    path('error/', views.investorerror, name='investorerror'),
    path('investors/', views.logout, name='logout')
] 