from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def string1(request):
    return HttpResponse('<h1><b>first view with response as a string</b></h1>')
def string2(request):
    return HttpResponse('<h1><i>second view with response as a string</i></h1>')