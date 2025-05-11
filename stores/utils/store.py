import json
from django.http import JsonResponse
from stores.models import Store
from stores.serializers import serialize_store
from app.utils import get_json_from_request_body


def stores_exception_to_json(exception):
    """
    Converts raw exception messages into user-friendly JSON error responses.
    """
    exception = str(exception)

    ERROR_MESSAGE_MAP = {
        "NOT NULL constraint failed: stores_store.name": "Invalid input. Insert a pair of key/value 'name': 'store name' "
    }

    if exception in ERROR_MESSAGE_MAP:
        return {"error": ERROR_MESSAGE_MAP[exception]}

    return exception


def create_new_store(request, response):
    """
    Create (POST) new store based on request body
    """
    try:
        request_body = get_json_from_request_body(request)
        new_store = Store.objects.create(
            name=request_body.get('name')
        )

        new_store.full_clean()
        new_store.save()
        
        response.append(serialize_store(new_store))
        return JsonResponse(response, safe=False, status=201)

    except Exception as e:
        response.append(stores_exception_to_json(e))
        return JsonResponse(response, safe=False, status=400)


def get_store_detail(response, store_id):
    """
    GET a single store
    """
    try:
        store = Store.objects.get(id=store_id)
        response.append(serialize_store(store))
        return JsonResponse(response, safe=False, status=200)

    except Exception as e:
        response.append(stores_exception_to_json(e))
        return JsonResponse(response, safe=False, status=400)


def update_store(request, response, store_id):
    """
    Use request body data given to UPDATE the store based on store_id given
    """
    try:
        request_body = get_json_from_request_body(request)
        store = Store.objects.get(id=store_id)
        store.name = request_body.get("name", store.name)
        store.save()

        response.append(serialize_store(store))
        return JsonResponse(response, safe=False, status=204)
    except Exception as e:
        response.append(stores_exception_to_json(e))
        return JsonResponse(response, safe=False, status=400)


def delete_store(response, store_id):
    """
    DELETE store based on id given
    """
    try:
        store = Store.objects.get(id=store_id)
        store.delete()
        return JsonResponse(response, safe=False, status=204)
    except Exception as e:
        response.append(stores_exception_to_json(e))
        return JsonResponse(response, safe=False, status=400)
