from django.urls import path
from .views import  login_View , signupView

urlpatterns=[
    path('',login_View,name='login'),
    path('',signupView, name='signup')
   
]