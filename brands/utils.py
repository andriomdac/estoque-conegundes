import json
from .models import Brand
from brands.serializers import serialize_brand
from app.utils.db_ops import serialize_model_list
from app.utils.http import (
    get_json_from_request_body,
    build_json_response,
    build_json_error_response,
    bad_request
    )
from app.utils.validators import (
    validate_request_body,
    validate_model_object_unique_name,
    validate_model_object_id,
    validate_and_save_model_object
    )
from app.utils.exceptions import (
    FieldValidationError,
    NotFoundValidationError,
    ObjectValidationError
    )


def create_new_brand(request, response):
    """
    Create (POST) new brand based on request body
    """
    try:
        data = validate_request_body(request, required_fields=["name"])
        name = validate_model_object_unique_name(data['name'], Brand, 'brand')
        new_brand = validate_and_save_model_object(Brand(name=name))
        return build_json_response(response, serialize_brand(new_brand), status=201)

    except (ValueError, FieldValidationError, ObjectValidationError) as e:
        return build_json_error_response(response, e, 400)


def update_brand(request, response, brand_id):
    """
    Use request body data given to UPDATE the brand based on brand_id given
    """
    try:
        data = validate_request_body(request)
        brand = validate_model_object_id(brand_id, Brand, 'brand')

        if 'name' in data:
            name = validate_model_object_unique_name(data['name'], Brand, 'brand')
            brand.name = name

        brand = validate_and_save_model_object(brand)
        return build_json_response(response, serialize_brand(brand), 200)

    except (ValueError, FieldValidationError, ObjectValidationError) as e:
        return build_json_error_response(response, e, 400)
    except NotFoundValidationError as e:
        return build_json_error_response(response, e, 404)