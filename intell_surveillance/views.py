from django.shortcuts import render

# Create your views here.


def product_suite(request):
    """ A view to return the product suite page """

    return render(request, 'intell_surveillance/product-suite.html')


def applications(request):
    """ A view to return the applications page """

    return render(request, 'intell_surveillance/applications.html')


def case_studies(request):
    """ A view to return the case studies page """

    return render(request, 'intell_surveillance/case-studies.html')
