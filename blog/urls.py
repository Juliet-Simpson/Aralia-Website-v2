from django.urls import path
from . import views

urlpatterns = [
    # path('', views.PostList.as_view(), name='blog'),
    path('', views.blog, name='blog'),
    path('<slug:slug>/<id>/', views.post_detail, name='post_detail'),
] 