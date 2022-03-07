from django.shortcuts import render

# Create your views here.


def surfacescanner(request):
    """ A view to return the index page """

    return render(request, 'surfacescanner/surfacescanner.html')