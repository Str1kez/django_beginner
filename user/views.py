from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import render, redirect

# Create your views here.
from user.forms import RegistrationForm


def sign_up(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # login(request, form)
            messages.success(request, 'Регистрация прошла успешно')
            # TODO: fix this
            # redirect('news:home')
        else:
            messages.error(request, 'Ошибка в регистрации')
    else:
        form = RegistrationForm()
    return render(request, 'user/sign_up.html', {'form': form})

