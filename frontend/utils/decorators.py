from .token import verify_token
from functools import wraps
from django.shortcuts import redirect


def token_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if verify_token(request.session.get('token')):
            return view_func(request, *args, **kwargs)
        else:
            return redirect("login")
    return wrapper