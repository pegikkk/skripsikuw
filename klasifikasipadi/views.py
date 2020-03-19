from django.shortcuts import render, redirect
from klasifikasipadi import models
from django.http import HttpResponse, Http404

def pengujian (request):
    return render(request, 'klasifikasipadi/index.html')


# Create your views here.
