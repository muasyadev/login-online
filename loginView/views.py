from django.shortcuts import render,redirect
from .forms import  Login_View , SignupView
from django.http import HttpResponse
from django.contrib.auth.models import User , auth
from django.contrib import messages
from .models import credentials

# Create your views here.


def login_View(request):
    if request.method == 'POST':
        form = Login_View(request.POST)
        if form.is_valid():
            # Process the login form data
            # Redirect or perform other actions
            return redirect('login_success')  # Replace with your desired URL name
    else:
        form = Login_View()

    return render(request, 'login_View.html', {'login_View': form, 'signupView': SignupView()})

def signupView(request):
    if request.method == 'POST':
        form = SignupView(request.POST)
        if form.is_valid():
            # Process the signup form data
            # Redirect or perform other actions
            return redirect('signup_success')  # Replace with your desired URL name
    else:
        form = SignupView()

    return render(request, 'login_View.html', {'login_View': Login_View(), 'signupView': form})
