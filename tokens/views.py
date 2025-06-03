from app.utils.validators import validate_request_body, validate_str_value_field
from app.utils.http import build_json_error_response, build_json_response, method_not_allowed
from app.utils.exceptions import FieldValidationError
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from .utils import verify_token 

from icecream import ic
from app.settings import JWT_SECRET_KEY
import jwt
from datetime import datetime, timedelta
import json
from jwt.exceptions import (
    ExpiredSignatureError,
    DecodeError,
    )


@csrf_exempt
def get_token_view(request):
    response = []

    if request.method == "POST":
        try:
            data = validate_request_body(request, required_fields=["username", "password"])

            username = validate_str_value_field(data['username'], 'username')
            password = validate_str_value_field(data['password'], 'password')

            user = authenticate(request, username=username, password=password)
            if user:
                exp = datetime.now() + timedelta(seconds=60)
                payload = {
                    "exp": exp.timestamp(),
                    "sub": f"{user.pk}"
                    }
                token = jwt.encode(payload=payload, key=JWT_SECRET_KEY, algorithm="HS256")
                data = {"token": token}

                return build_json_response(response, data, 201)
            
            return build_json_error_response(response, "invalid credentials")

        except (ValueError, FieldValidationError) as e:
            return build_json_error_response(response, e, 400)
    return method_not_allowed(response)


@csrf_exempt
def verify_token_view(request):
    response = []

    if request.method == "POST":
        return verify_token(
            request=request,
            response=response
            )

    return method_not_allowed(response)