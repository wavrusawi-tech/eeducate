from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def role_select(request):
    return render('request', 'login/role.html')
def welcome(request):
    return render('request', 'login/index.html')