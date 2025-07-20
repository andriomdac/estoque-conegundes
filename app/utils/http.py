import json
from django.http import JsonResponse


def get_json_from_request_body(request):
    """
    Parses and returns JSON data from the HTTP request body.
    """
    return json.loads(request.body.decode('utf-8'))


def build_json_response(response, data=None, status=200):
    """
    Appends data to the response list and returns a JsonResponse with the full response.
    """
    if data:
        response.append(data)
    return JsonResponse(response, safe=False, status=status)


def build_json_error_response(response, message="", status=500):
    if message:
        return build_json_response(response, {"error": str(message)}, status=status)
    return build_json_response(response, status=status)


def method_not_allowed(response):
    """
    Return 405 (Method Not Allowed) to Response
    """
    error_message = {"error": "Method not allowed"}
    return build_json_response(response, error_message, status=405)


def bad_request(response):
    """
    Return 400 (Bad Request) to Response
    """
    return build_json_error_response(response, "bad request", status=400)