from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name='core'

urlpatterns = [
    path('', views.index, name='index'),
    path('submit/', views.submit, name='submit'),
    path('login2038/', views.admin, name='admin'),
    path('2038login/', views.AdminLogin, name='adminLogin'),
]