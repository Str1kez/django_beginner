from django.contrib import messages
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect

# Create your views here.
from user.forms import RegistrationForm, AuthForm


def sign_up(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Регистрация прошла успешно')
            return redirect('news:home')
        else:
            messages.error(request, 'Ошибка в регистрации')
    else:
        form = RegistrationForm()
    return render(request, 'user/sign_up.html', {'form': form})


def sign_in(request):
    if request.method == 'POST':
        form = AuthForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            messages.success(request, f'Вы вошли в аккаунт как {form.get_user().username}')
            return redirect('news:home')
        else:
            messages.error(request, 'Ошибка при входе')
    else:
        form = AuthForm()
    return render(request, 'user/sign_in.html', {'form': form})


def user_logout(request):
    logout(request)
    messages.success(request, 'Вы вышли из аккаунта')
    return redirect('news:home')
