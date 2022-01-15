from django.urls import path

from user.views import sign_up, sign_in, user_logout

app_name = 'user'

urlpatterns = [
    path('sign_up', sign_up, name='sign_up'),
    path('sign_in', sign_in, name='sign_in'),
    path('logout', user_logout, name='logout')
]
