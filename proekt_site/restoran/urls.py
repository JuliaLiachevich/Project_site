from django.urls import path
from . import views

urlpatterns = [
    path('', views.text, name='restoran'),
    path('food/', views.reg_food, name='food'),
    path('register/', views.reg_restoran, name='register'),
    path('<int:pk>/', views.AboutDetailView.as_view(), name='about'),

]