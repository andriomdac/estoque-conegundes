from app.utils.http import build_json_error_response, build_json_response
import jwt
from app.settings import JWT_SECRET_KEY
from functools import wraps


def token_required(view_func):
    @wraps(view_func)

    def wrapped_view(request, *args, **kwargs):
        token = request.headers.get("Authorization")
        response = []

        try:
            if token:
                if token.startswith("Bearer "):
                    token = token[7:] # Remove "Bearer " from the beginning of the Authorization field
                decoded_token = jwt.decode(token, key=JWT_SECRET_KEY, algorithms="HS256")
                return view_func(request, *args, **kwargs)
            return build_json_error_response(response, "Token not provided", status=400)

        except jwt.ExpiredSignatureError:
            return build_json_error_response(response,  "Token expired", status=400)
        except jwt.DecodeError:
            return build_json_error_response(response, "Invalid token", status=400)

    return wrapped_view