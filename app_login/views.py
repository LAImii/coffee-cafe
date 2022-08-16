import re

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
# from django.contrib.auth.decorators import login_required

from app_login.forms import RegisterModelForm, LoginModelForm

# Create your views here.
# @login_required(login_url='login')
# Homepage
def home(request):
    return render(request, 'app_login/home.html')

# Register page
def register(request):
    if request.user.is_authenticated:
        return render(request, 'app_login/home.html')
    else:
        register_form = RegisterModelForm()
        if request.method == 'POST':
            form = RegisterModelForm(request.POST)
            if form.is_valid():
                form.save()
                # user = form.cleaned_data.get('username')
                # messages.success((request), 'Account was created for ' + user)
                return HttpResponseRedirect(reverse('register_complete'))
            else:
                password1 = request.POST.get('password1')
                password2 = request.POST.get('password2')
                if password1 != password2:
                    messages.info(request, "The password confirmation doesn't match.")
                elif len(password1) <= 8:
                    messages.info(request, "Passwords must be at least 8 characters in length and contain letters, numerics, and special characters.")
                elif re.findall("[\W]", password1) == []:
                    messages.info(request, "Passwords must be at least 8 characters in length and contain letters, numerics, and special characters.")
                elif re.findall("[\d]", password1) == []:
                    messages.info(request, "Passwords must be at least 8 characters in length and contain letters, numerics, and special characters.")
                elif re.findall("[A-z]", password1) == []:
                    messages.info(request, "Registration failed! Please try again later.")
                else:
                    messages.info(request, "Registration failed! Please try again.")
        context = {'form': register_form}
        return render(request, 'app_login/register_form.html', context)

# Login page
def login(request):
    if request.user.is_authenticated:
        return render(request, 'app_login/home.html')
    else:
        login_form = LoginModelForm()
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('home')
            else:
                messages.info(request, "Username and/or Password is incorrect.")
        context = {'form': login_form}
        return render(request, 'app_login/login_form.html', context)

# registered completely page
def register_complete(request):
    if request.user.is_authenticated:
        return render(request, 'app_login/home.html')
    else:
        return render(request, 'app_login/register_complete.html')

# logout page
def logout(request):
    auth_logout(request)
    return redirect('login')