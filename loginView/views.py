from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User , auth
from django.contrib import messages
from .models import credentials

# Create your views here.
def loginView(request):
  
         return render(request,'loginView.html')