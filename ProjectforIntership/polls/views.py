from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def hellomicky(request):
    return HttpResponse('Hello. i`m Micky')

def fine(request):
    return HttpResponse('I`M FINE')