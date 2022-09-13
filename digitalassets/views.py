from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_GET
import json

# Create your views here.

def digital_assets(request):
    """ A view to return the case studies page """
    responseData = {
        'id' : 'test',
        'name' : 'Daniel',
        'age' : 100
    }
    return HttpResponse(json.dumps(responseData), context_type="application/json")
