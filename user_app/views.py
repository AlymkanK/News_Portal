from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserSignInForm


def user_register_view(request):
    if request.method == 'POST':
        reg_form = UserRegisterForm(request.POST)
        if reg_form.is_valid():
            username = reg_form.cleaned_data.get['username']
            first_name = reg_form.cleaned_data.get['first_name']
            last_name = reg_form.cleaned_data.get['last_name']
            password = reg_form.cleaned_data.get['password']
            if User.objects.filter(username=username).exists():
                reg_form.add_error('username', f'пользователь для {username} уже существует')
            else:
                user = User.objects.create_user(
                    username=username,
                    first_name = first_name,
                    last_name = last_name,
                    password = password,
                )
                user.is_active = True
                user.save()
                authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, f'Account was created for {username}')
                    return redirect('article_app:articles')
    else:
        reg_form = UserRegisterForm()

    context = {
        'reg_form': reg_form
    }
    return render(request, 'user_app/register.html', context)



def user_sign_in_view(request):
    if request.method == 'POST':
        sign_in_form = UserSignInForm(request.POST)
        if sign_in_form.is_valid():
            username = sign_in_form.cleaned_data.get['username']
            password = sign_in_form.cleaned_data.get['password']

            user = User.objects.get(
                username = username,
                password = password
            )
            user.is_active = True
            authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('article_app:articles')
    else:
        sign_in_form = UserSignInForm()

    context = {
        'sign_in_form': sign_in_form
    }
    return render(request, 'user_app/login.html', context)



@login_required
def logout_user(request):
    logout(request)
    messages.success(request, 'Вы успешно вышли из аккаунта')
    return redirect('article_app:articles')

