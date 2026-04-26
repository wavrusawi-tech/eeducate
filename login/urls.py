from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name="login"

urlpatterns = [
    path('roles/', views.role_select, name='roleView'),
    path('', views.welcome, name='welcomeView')
]