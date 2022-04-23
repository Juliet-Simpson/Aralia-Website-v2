from django.urls import path
from . import views

urlpatterns = [
    path('product-suite/', views.product_suite, name='product-suite'),
    path('applications/', views.applications, name='applications'),
    path('case-studies/', views.case_studies, name='case-studies'),
] 