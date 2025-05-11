import json
from django.http import JsonResponse


def serialize_model_list(model_class, exception_to_json_func, serializer_func, response):
    """
    Serializes a queryset of model instances into JSON response.

    Retrieves all instances of the specified model class, serializes each one using
    the provided serializer function, and returns them as a JSON response. Handles
    any exceptions by processing them with the exception function and returning
    an error response.

    Args:
        model_class (Model): Django model class to query for objects
        exception_to_json_func (function): Function to process exceptions, should accept
                                  an exception and return error data
        serializer_func (function): Function to serialize model instances, should
                                   accept a model instance and return serialized data
        response (list): Initial list to which serialized data will be appended

    Returns:
        JsonResponse: Response containing either:
                     - Serialized objects (status 200) on success
                     - Error information (status 400) on failure

    Note:
        The response parameter is modified in-place by appending serialized data or errors.
    """
    try:
        objects = model_class.objects.all()
        for obj in objects:
            response.append(serializer_func(obj))
        return JsonResponse(response, safe=False, status=200)

    except Exception as e:
        response.append(exception_to_json_func(e))
        return JsonResponse(response, safe=False, status=400)


def get_json_from_request_body(request):
    """
    Parses and returns JSON data from the HTTP request body.
    """
    return json.loads(request.body.decode('utf-8'))


def method_not_allowed(response):
    """
    Return 405 (Method Not Allowed) to Response
    """
    response.append({"error": "Method not allowed"})
    return JsonResponse(response, safe=False, status=405)
