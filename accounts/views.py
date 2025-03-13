from django.shortcuts import render
from django.views.generic import CreateView
from accounts.forms import RegisterForm, LoginForm
from accounts.models import User
from django.contrib.auth.views import LoginView

class RegisterView(CreateView):
    model = User
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = '/accounts/login/'


class LoginUser(LoginView):
     
    template_name = 'login.html'
    form_class = LoginForm
    success_url = '/'


