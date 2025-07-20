from app.utils.http import build_json_error_response, build_json_response
import jwt
from app.settings import JWT_SECRET_KEY
from functools import wraps
from icecream import ic


def verify_token(request, response):
    token = request.headers.get("Authorization")
    try:
        if token:
            if token.startswith("Bearer "):
                token = token[7:] # Removes the 'Bearer ' from the beginning of the "Authorization" header field
            decoded_token = jwt.decode(token, key=JWT_SECRET_KEY, algorithms="HS256")
            return build_json_response(response, status=200)
        return build_json_error_response(response, "Token not provided", 400)

    except (jwt.ExpiredSignatureError, jwt.DecodeError) as e:
        return build_json_error_response(response, e, 400)