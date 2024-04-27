from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def female(request):
    return HttpResponse('THIS PAGE ONLY FOR WOMEN!!!')
