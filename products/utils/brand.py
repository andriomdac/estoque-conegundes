import json
from django.http import JsonResponse
from products.models import Brand
from products.serializers import serialize_brand
from app.utils import get_json_from_request_body
from icecream import ic


def brands_exception_to_json(exception):
    """
    Converts raw exception messages into user-friendly JSON error responses.
    """
    exception = str(exception)
    ERROR_MESSAGE_MAP = {}
    if exception in ERROR_MESSAGE_MAP:
        return {"error": ERROR_MESSAGE_MAP[exception]}
    return exception


def create_new_brand(request, response):
    """
    Create (POST) new brand based on request body
    """
    try:
        request_body = get_json_from_request_body(request)
        name = request_body['name']

        new_brand = Brand.objects.create(
            name=name,
        )

        new_brand.full_clean()
        new_brand.save()
        
        response.append(serialize_brand(new_brand))
        return JsonResponse(response, safe=False, status=201)

    except Exception as e:
        response.append(brands_exception_to_json(e))
        return JsonResponse(response, safe=False, status=400)


def get_brand_detail(response, brand_id):
    """
    GET a single brand
    """
    try:
        brand = Brand.objects.get(id=brand_id)
        response.append(serialize_brand(brand))
        return JsonResponse(response, safe=False, status=200)

    except Exception as e:
        response.append(brands_exception_to_json(e))
        return JsonResponse(response, safe=False, status=400)


def update_brand(request, response, brand_id):
    """
    Use request body data given to UPDATE the brand based on brand_id given
    """
    try:
        request_body = get_json_from_request_body(request)
        brand = Brand.objects.get(id=brand_id)
        brand.name = request_body.get("name", brand.name)
        brand.save()

        response.append(serialize_brand(brand))
        return JsonResponse(response, safe=False, status=204)
    except Exception as e:
        response.append(brands_exception_to_json(e))
        return JsonResponse(response, safe=False, status=400)


def delete_brand(response, brand_id):
    """
    DELETE brand based on id given
    """
    try:
        brand = Brand.objects.get(id=brand_id)
        brand.delete()
        return JsonResponse(response, safe=False, status=204)
    except Exception as e:
        response.append(brands_exception_to_json(e))
        return JsonResponse(response, safe=False, status=400)
