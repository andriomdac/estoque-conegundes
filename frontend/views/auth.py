from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from frontend.utils.token import get_token
import requests
import json
from icecream import ic


def login_view(request):
    context = {}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        jwt_response = get_token(username, password)

        if 'token' in jwt_response:
            request.session['token'] = jwt_response['token']
            return redirect('home')

        if 'error' in jwt_response:
            context['login_error'] = "Credenciais Inválidas. Verifique seu usuário e senha."

    return render(request, "auth/login.html", context)


def logout_view(request):
    if 'token' in request.session:
        del request.session['token']
    return redirect('login')