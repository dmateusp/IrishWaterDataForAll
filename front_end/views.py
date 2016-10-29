from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, you are on the main page")
# Create your views here.
