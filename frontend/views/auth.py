from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
import requests
import json
from icecream import ic


API_LOCAL_HOST = "http://localhost:8000/api/"


def get_token(username:str, password:str) -> dict:
    response = requests.post(
        url=API_LOCAL_HOST+"auth/get_token/",
        json={"username": username, "password": password}
        ).content
    return json.loads(response)[0]


def verify_session_token(request, token:str) -> dict:
    if 'token' in request.session:
        response = requests.post(
            API_LOCAL_HOST+"auth/verify_token/",
            headers={"Authorization": request.session['token']},
        ).content
    
        response = json.loads(response)
        ic(response)
    redirect('login')
    


def login_view(request):
    context = {}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        jwt_response = get_token(username, password)

        if 'token' in jwt_response:
            request.session['jwt'] = jwt_response
            return redirect('home')

        if 'error' in jwt_response:
            context['login_error'] = "Credenciais Inválidas. Verifique seu usuário e senha."

    return render(request, "auth/login.html", context)


def logout_view(request):
    if 'token' in request.session:
        del request.session['token']
    return redirect('login')