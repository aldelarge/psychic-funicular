# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'main/home.html')

def salvation(request):
    return render(request, 'main/salvation.html')

def gospel(request):
    return render(request, 'main/gospel.html')

def book1(request):
    return render(request, 'main/book1.html')

def AboutUs(request):
    return render(request, 'main/AboutUs.html')
