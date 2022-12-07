from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib import messages
from django.contrib.auth.models import User



def register(request):
    if request.method == 'GET':
        form = UserRegistrationForm()
        return render(request, 'accounts/register.html', {'form':form})

    else:
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(**form.cleaned_data)
            messages.success(request, 'Registered', 'success')
            return redirect('todo:home')
        else:
            return HttpResponse(f'{form.errors}')

def user_login(request):
    if request.method == 'GET':
        form = UserLoginForm()
        return render(request, 'accounts/login.html', {'form':form})

    else:
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, **cd)
            if user:
                login(request, user)
                messages.success(request, 'Logged in', 'success')
                return redirect('todo:home')
            else:
                return HttpResponse('Wrong User/Pass')
        else:
            return HttpResponse(f'{form.errors}')


def user_logout(request):
	logout(request)
	messages.success(request, 'logged out successfully', 'success')
	return redirect('todo:home')