# Create your views here.

from models import *
from forms import *

from django.template.loader import get_template
from django.template import Context, RequestContext
from django.shortcuts import render_to_response
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.core.serializers import serialize
from django.views.decorators.csrf import csrf_exempt
from django.utils import simplejson

def main(request):
    
    return render_to_response('pothole.html', 
                              {'title': 'pghpotholes'},
                              context_instance=RequestContext(request))
    
@csrf_exempt
def getdata(request):
    
    all_potholes = Pothole.objects.all()
    data = []
    for pothole in all_potholes:
        data.append({'lat': pothole.lat,
                     'lng': pothole.long})
        
    if request.is_ajax():
        return HttpResponse(simplejson.dumps(data), "application/json")