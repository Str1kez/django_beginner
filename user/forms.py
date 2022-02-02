from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms


css_attr = {'class': 'form-control', 'id': 'exampleInputEmail1'}


class RegistrationForm(UserCreationForm):
    username = forms.CharField(required=True,
                               widget=forms.TextInput(attrs=css_attr),
                               label='Имя пользователя')
    email = forms.EmailField(widget=forms.EmailInput(attrs=css_attr))
    password1 = forms.CharField(required=True,
                                widget=forms.PasswordInput(attrs=css_attr),
                                label='Пароль')
    password2 = forms.CharField(required=True,
                                widget=forms.PasswordInput(attrs=css_attr),
                                label='Подтвердить пароль')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class AuthForm(AuthenticationForm):
    username = forms.CharField(required=True,
                               widget=forms.TextInput(attrs=css_attr),
                               label='Имя пользователя')
    password = forms.CharField(required=True,
                               widget=forms.PasswordInput(attrs=css_attr),
                               label='Пароль')
