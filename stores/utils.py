import json
from django.http import JsonResponse
from .models import Store
from .serializers import serialize_store
from app.utils.http import build_json_response, build_json_error_response
from django.core.validators import ValidationError
from app.utils.validators import validate_request_body
from app.utils.exceptions import DuplicateStoreException
from stores.validators import validate_store_name


def create_new_store(request, response):
    """
    Create (POST) new store based on request body
    """
    try:
        data = validate_request_body(request, required_fields=["name",])
    except ValueError as e:
        return build_json_error_response(response, e, status=400)

    try:
        name = validate_store_name(data['name'])
    except DuplicateStoreException as e:
        return build_json_error_response(response, e, status=400)
    except ValueError as e:
        return build_json_error_response(response, e, status=400)

    try:
        new_store = Store(name=name)
        new_store.full_clean()
        new_store.save()
        return build_json_response(response, serialize_store(new_store), status=201)

    except ValidationError as e:
        return build_json_error_response(response, e.message_dict, status=400)



def update_store(request, response, store_id):
    """
    Use request body data given to UPDATE the store based on store_id given
    """
    try:
        data = validate_request_body(request)
    except ValueError as e:
        return build_json_error_response(response, e, status=400)

    if 'name' in data:
        try:
            name = validate_store_name(data['name'])
        except DuplicateStoreException as e:
            return build_json_error_response(response, e, status=400)
    
    try:
        store = Store.objects.get(id=store_id)
        store.name = name
        store.full_clean()
        store.save()
        return build_json_response(response, serialize_store(store))

    except ValidationError as e:
        return build_json_error_response(response, e.message_dict, status=400)
    except Store.DoesNotExist as e:
        return build_json_error_response(response, e, 404)
