from django.urls import path
from . import views
from restoran.views import bezlactoz, diabet, bezgluten, vegan, allergia_prod

urlpatterns = [
    path('', views.info, name='home'),
    path('allergia/', views.allergia, name='allergia'),
    path('diabet/', diabet, name='diabet'),
    path('bezgluten/', bezgluten, name='bezgluten'),
    path('vegan/', vegan, name='vegan'),
    path('bezlactoz/', bezlactoz, name='bezlactoz'),
    path('allergia2/', allergia_prod, name='allergia2'),

]
