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


def investors(request):
    """ A view show the investor login page (or investors page if a correct password is in session) and load the investors page if a correct password is entered. Also set a session variable that staylogged is ture if the stay logged in box is checked"""
    print(request.session.items())
    if request.session.get('staylogged') == True:

        return render(request, 'home/investors.html')
    else:
        if (request.method == 'POST'):
            password = request.POST.get("password")
            staylogged = request.POST.get("staylogged")
            if (password == os.environ.get('INVESTOR_PASSWORD')):
                if staylogged:
                    request.session['staylogged'] = True
                return render(request, 'home/investors.html')
            else:
                return redirect('investorerror')

        return render(request, 'home/investorlogin.html')


def logout(request):
    """A view to change the staylogged in session variable to false and return to the login page"""
    request.session['staylogged'] = False
    print(request.session.items())
    return redirect('investors')

def investorerror(request):
    """A view to display the login with an error message after an incorrect password attempt"""

    if (request.method == 'POST'):
        password = request.POST.get("password")
        staylogged = request.POST.get("staylogged")
        if (password == os.environ.get('INVESTOR_PASSWORD')):
            if staylogged:
                request.session['staylogged'] = {
                    'staylogged': True
                }
            return render(request, 'home/investors.html')
        else:
            return redirect('investorerror')

    context = {
        "error": True 
    }
    return render(request, 'home/investorlogin.html', context)
    
