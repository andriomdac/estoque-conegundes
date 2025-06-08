from django.shortcuts import render
from .auth import verify_session_token
from icecream import ic


def home(request):
    ic(verify_session_token(request, request.session.get('jwt')))
    return render(request, "base.html")