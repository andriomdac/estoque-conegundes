import json
from django.http import JsonResponse
from .models import Brand
from brands.serializers import serialize_brand
from app.utils.http import (
    get_json_from_request_body,
    build_json_response,
    bad_request
    )
from app.utils.db_ops import serialize_model_list
from django.core.exceptions import ValidationError
from django.db.models.deletion import ProtectedError


def create_new_brand(request, response):
    """
    Create (POST) new brand based on request body
    """
    try:
        data = get_json_from_request_body(request)
    except json.JSONDecodeError:
        return build_json_response(response, {"error": "invalid request body"}, status=400)

    name = data.get('name')

    if name:
        new_brand = Brand.objects.create(
            name=name
        )
        new_brand.full_clean()
        new_brand.save()
        return build_json_response(response, serialize_brand(new_brand), status=201)

    return build_json_response(
        response,
        {
            "error": "Field 'name' invalid or missing.",
            "expected structure": {
                "name": "brand_name"
                }},
        status=400)


def update_brand(request, response, brand_id):
    """
    Use request body data given to UPDATE the brand based on brand_id given
    """
    try:
        data = get_json_from_request_body(request)
    except json.JSONDecodeError:
        return build_json_response(response, {"error": "invalid request body"}, status=400)

    new_name = data.get('name')

    if not new_name:
        return build_json_response(
            response,
            {
                "error": "field 'name' required.",
                "expected structure": {
                    "name": "brand_name"
                    }},
            status=400)

    try:
        brand = Brand.objects.get(id=brand_id)
        brand.name = new_name
        brand.full_clean()
        brand.save()
        return build_json_response(response, serialize_brand(brand), 200)

    except ValidationError as e:
        return build_json_response(response, {"error": e.message_dict}, status=400)
    except Brand.DoesNotExist:
        return build_json_response(response, {"error": "Brand not found."}, status=404)