# Almost all reusable functions for crub operations in database.
# Create objects, Update, Delete etc... with exceptions and errors handlers.

from django.db.models.deletion import ProtectedError
from django.http import JsonResponse
from app.utils.http import build_json_error_response, build_json_response


def delete_model_object(response, object_id, model_class, object_name):
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