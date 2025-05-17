import json
from django.http import JsonResponse
from .models import Brand
from brands.serializers import serialize_brand
from app.utils.http import (
    get_json_from_request_body,
    build_json_response,
    build_json_error_response,
    bad_request
    )
from app.utils.db_ops import serialize_model_list
from django.core.exceptions import ValidationError
from django.db.models.deletion import ProtectedError
from app.utils.validators import validate_request_body
from .validators import validate_brand_name


def create_new_brand(request, response):
    """
    Create (POST) new brand based on request body
    """
    try:
        data = validate_request_body(request, required_fields=["name"])
    except ValueError as e:
        return build_json_error_response(response, e, 400)

    try:
        name = validate_brand_name(data['name'])
    except ValueError as e:
        return build_json_error_response(response, e, 400)

    try:
        new_brand = Brand(
            name=name
        )
        new_brand.full_clean()
        new_brand.save()
        return build_json_response(response, serialize_brand(new_brand), status=201)
    except ValidationError as e:
        return build_json_error_response(response, e.message_dict, 400)


def update_brand(request, response, brand_id):
    """
    Use request body data given to UPDATE the brand based on brand_id given
    """
    try:
        data = validate_request_body(request)
    except ValueError as e:
        return build_json_error_response(response, e, 400)
    
    if 'name' in data:
        try:
            name = validate_brand_name(data['name'])
        except ValueError as e:
            return build_json_error_response(response, e, 400)

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