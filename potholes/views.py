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

from potholes import tasks
from threading import Thread

print 'fooo'

twitter_thread = Thread(target=tasks.twist_listener)
twitter_thread.setDaemon(True)
twitter_thread.start()

def main(request):
    
    return render_to_response('pothole.html', 
                              {'title': 'pghpotholes'},
                              context_instance=RequestContext(request))
    
    
def getdata(request):
    
    pass