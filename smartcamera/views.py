from django.shortcuts import render

# Create your views here.


def smartcamera(request):
    """ A view to return the index page """

    return render(request, 'smartcamera/smartcamera.html')
    