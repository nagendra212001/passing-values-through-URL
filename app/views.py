from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.


def rowdy(request):
    return HttpResponse('good morning')

def rowdy(request,name):
    return HttpResponse( f'good morning {name}')