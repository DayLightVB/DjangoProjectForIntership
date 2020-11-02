from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def klo(request):
    return render(request, 'polls/klo.html')


def offers(request):
    return render(request, 'polls/offers.html')


def about(request):
    return render(request, 'polls/about.html')





