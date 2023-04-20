from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse
from app.models import *


def insert_Topic(request):
    TFO=TopicForm()
    d={'TFO':TFO}

    if request.method=="POST":
        TFDO=TopicForm(request.POST)
        if TFDO.is_valid():
            TFDO.save()
        return HttpResponse("topic is inserted successfully")    

    return render(request,'insert_Topic.html',d)

def insert_Webpage(request):
    WFO=WebpageForm()
    d={'WFO':WFO}

    if request.method=="POST":
        WFDO=WebpageForm(request.POST)
        if WFDO.is_valid():
            WFDO.save()
        return HttpResponse("webpage is inserted successfully")   
    return render(request,'insert_Webpage.html',d)

def insert_AccessRecord(request):
    ARO=AccessForm()
    d={'AFO':ARO}

    if request.method=="POST":
        ARDO=AccessForm(request.POST)
        if ARDO.is_valid():
            ARDO.save()
        return HttpResponse("Access records are inserted successfully")
    return render(request,'insert_AccessRecord.html',d)
