# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from models import Guest
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'guestbook_app/index.html')

def process(request):
    if(len(request.POST['name']) < 3):
        messages.error(request,"name too short")
        return redirect('/')
    else:
        Guest.objects.create(name=request.POST['name'])
        return redirect('/result')

def result(request):
    context = {
        'names' : Guest.objects.all()
    }

    return render(request, "guestbook_app/results.html",context)