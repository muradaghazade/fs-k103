from django.shortcuts import render
from django.views.generic import CreateView
from accounts.forms import RegisterForm
from accounts.models import User

class RegisterView(CreateView):
    model = User
    template_name = 'register.html'
    form_class = RegisterForm
