
from django import forms

class SignupView(forms.Form):
    # Signup form fields go here
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())


class Login_View(forms.Form):
    # Login form fields go here
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())