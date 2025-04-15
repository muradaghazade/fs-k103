from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from accounts.forms import *
from accounts.models import User
from django.contrib.auth.views import LoginView

class RegisterView(CreateView):
    model = User
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = '/accounts/login/'

class EditProfile(UpdateView):
    model = User
    template_name = 'edit_profile.html'
    form_class = EditProfileForm
    success_url = '/'

class LoginUser(LoginView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = '/'

def user_profile(request, id):
    user = User.objects.get(id=id)
    context = {
        'user': user,
    }
    return render(request, 'user-profile.html', context)

