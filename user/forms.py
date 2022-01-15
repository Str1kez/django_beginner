from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms


class RegistrationForm(UserCreationForm):
    username = forms.CharField(required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'exampleInputEmail1',
                                                             'autofocus': False}),
                               label='Имя пользователя')
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'id': 'exampleInputEmail1'}))
    password1 = forms.CharField(required=True,
                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'exampleInputEmail1'}),
                                label='Пароль')
    password2 = forms.CharField(required=True,
                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'exampleInputEmail1'}),
                                label='Подтвердить пароль')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class AuthForm(AuthenticationForm):
    username = forms.CharField(required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'exampleInputEmail1'}),
                               label='what?'),
    password = forms.CharField(required=True,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'exampleInputEmail1'}),
                               label='Пароль')
