from django.urls import path

from user.views import sign_up

urlpatterns = [
    path('sign_up', sign_up, name='sign_up'),
    # path('sign_in', sign_in, name='sign_in')
]
