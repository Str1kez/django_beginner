from django.contrib import messages
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.core.mail import EmailMessage

# Create your views here.
from user.forms import RegistrationForm, AuthForm, EmailForm
from myapp.settings import EMAIL_HOST_USER


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


def send_email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            message = EmailMessage(subject=form.cleaned_data['subject'],
                                   body=form.cleaned_data['content'],
                                   from_email=EMAIL_HOST_USER,
                                   to=[form.cleaned_data['destination_email']],
                                   )
            message.content_subtype = 'html'
            is_sent = message.send(fail_silently=True)
            if is_sent:
                messages.success(request, 'Письмо отправлено')
            else:
                messages.error(request, 'Ошибка отправки')
            return redirect('user:send_email')
    else:
        form = EmailForm()
    return render(request, 'user/send_email.html', {'form': form})
