from django.shortcuts import render, redirect
from icecream import ic
from frontend.utils.decorators import token_required


@token_required
def home(request):
    ic(request.session.get('token'))
    return render(request, "base.html")