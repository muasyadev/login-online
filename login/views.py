from django.shortcuts import render
from .models import credentials

# Create your views here.
def login(request):
    return render (request,'login.html')


