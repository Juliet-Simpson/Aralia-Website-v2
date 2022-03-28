from django.shortcuts import render, redirect
import os
if os.path.exists("env.py"):
    import env

# Create your views here.

def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def about(request):
    """ A view to return the about page """

    return render(request, 'home/about.html')


def investorlogin(request):
    """ A view show the investor login page (or investors page if a correct password is in session) and load the investors page if a correct password is entered"""

    if 'investor_password' in request.session:

        return redirect('investors')
    else:
        if (request.method == 'POST'):
            password = request.POST.get("password")
            if (password == os.environ.get('INVESTOR_PASSWORD')):
                request.session['investor_password'] = 'valid'
                return redirect('investors')
            else:
                return redirect('investorerror')

        return render(request, 'home/investorlogin.html')


def investorerror(request):
    """A view to display the login with an error message after an incorrect password attempt"""

    if (request.method == 'POST'):
        password = request.POST.get("password")
        if (password == "Investor1"):
            # doesn't work
            request.session['investor_password'] = 'valid'
            return redirect('investors')
        else:
            return redirect('investorerror')

    context = {
        "error": True 
    }
    return render(request, 'home/investorlogin.html', context)


def investors(request):
    """ A view to return the investors page """

    return render(request, 'home/investors.html')
