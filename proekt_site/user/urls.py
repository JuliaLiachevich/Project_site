from django.urls import path
from .views import *

urlpatterns = [
    path('', create, name='user'),
    path('login/', login, name='login_user'),
    path('logaut/', logaut, name='logaut'),
    path('register/', register, name='register_user'),

]