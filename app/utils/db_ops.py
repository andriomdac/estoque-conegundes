# All reusable functions for crub operations in database.
# Create objects, Update, Delete etc... with exceptions and errors handlers.

from django.db.models.deletion import ProtectedError
from django.http import JsonResponse
from app.utils.http import build_json_error_response, build_json_response


def delete_model_object(response, object_id, model_class, object_name):
    """
    Attempts to delete an object of the given model class by its ID.

    Retrieves the object using the provided ID, deletes it if found, and returns
    an appropriate JSON response. Handles cases where the object does not exist
    or cannot be deleted due to related references (e.g., foreign key constraints).

    Args:
        response: The HTTP response object or context used for building the JSON response.
        object_id (int): The ID of the object to delete.
        model_class (Django Model): The Django model class to query.
        object_name (str): The name of the object (used in error messages).

    Returns:
        JsonResponse: A response with:
            - 204 status if deletion is successful.
            - 404 status if the object is not found.
            - 400 status if deletion fails due to protected related objects.
    """
    try:
        obj = model_class.objects.get(id=object_id)
        obj.delete()
        return build_json_response(response, status=204)
    except model_class.DoesNotExist:
        return build_json_error_response(
            response,
            f"{object_name} not found",
            status=404
            )
    except ProtectedError:
        return build_json_error_response(
            response,
            f"Cannot delete {object_name} as it's referenced by other objects",
            status=400
            )


def serialize_model_list(response, model_class, serializer_func):
    objects = model_class.objects.all()
    for obj in objects:
        response.append(serializer_func(obj))
    return JsonResponse(response, safe=False, status=200)



def get_model_object_detail(response, object_id, model_class, serializer, object_name):
    """
    GET a single model object by ID given
    """
    try:
        obj = model_class.objects.get(id=object_id)
        return build_json_response(response, serializer(obj), 200)
    except model_class.DoesNotExist:
        return build_json_error_response(response, f"{object_name} '{object_id}' does not exist.", status=404)