from django.shortcuts import render, get_object_or_404
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


def post_detail(request, slug, id):
    """docstring"""

    post_list = Post.objects.filter(status=1).order_by('-created_on')
    post = get_object_or_404(Post, pk=id)

    context = {
        "post_list": post_list,
        "post": post
    }

    return render(request, 'blog/post_detail.html', context)

