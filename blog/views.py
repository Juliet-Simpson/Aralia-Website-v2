from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.

def blog(request):
    """docstring"""

    post_list = Post.objects.filter(status=1).order_by('-created_on')

    context = {
        "post_list": post_list
    }

    return render(request, 'blog/post_list.html', context)


class PostDetail(generic.DetailView):
    """docstring"""
    model = Post
    template_name = 'blog/post_detail.html'

