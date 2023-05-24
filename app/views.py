from django.shortcuts import render

# Create your views here.

from app.models import *

def display_topics(request):

    LTO=Topic.objects.all()
    d={'LTO':LTO}

    return render(request,'display_topics.html',d)

def display_web(request):

    LWO=Webpage.objects.all()
    d={'LWO':LWO}

    return render(request,'display_web.html',d)

def display_access(request):

    LAO=Access.objects.all()
    d={'LAO':LAO}

    return render(request,'display_access.html',d)