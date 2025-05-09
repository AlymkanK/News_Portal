from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, UserCreationForm, UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get['username']
            if User.objects.filter(username=username).exists:
                form.add_error('username', f'пользователь для {username} уже существует')
            else:
                messages.success(request, f'Account was created for {username}')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/profile.html')


@login_required
def profile(request):
    return render(request, 'users/profile.html')

