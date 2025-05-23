import json
from .models import Category
from categories.serializers import serialize_category
from app.utils.http import (
    get_json_from_request_body,
    build_json_response,
    build_json_error_response,
    bad_request
    )
from app.utils.db_ops import serialize_model_list
from app.utils.validators import (
    validate_request_body,
    validate_model_object_id,
    validate_model_object_unique_name,
    validate_and_save_model_object
    )
from app.utils.exceptions import (
    FieldValidationError,
    NotFoundValidationError,
    ObjectValidationError
    )


def create_new_category(request, response):
    """
    Create (POST) new category based on request body
    """
    try:
        data = validate_request_body(request, required_fields=['name'])
        name = validate_model_object_unique_name(data['name'], Category, 'category')
        new_category = validate_and_save_model_object(Category(name=name))
        return build_json_response(response, serialize_category(new_category), 201)

    except (ValueError, FieldValidationError, ObjectValidationError) as e:
        return build_json_error_response(response, e, 400)



def update_category(request, response, category_id):
    """
    Use request body data given to UPDATE the brand based on brand_id given
    """
    try:
        data = validate_request_body(request)
        category = validate_model_object_id(category_id, Category, 'category')

        if 'name' in data:
            name = validate_model_object_unique_name(data['name'], Category, 'category')
            category.name = name

        category = validate_and_save_model_object(category)
        return build_json_response(response, serialize_category(category), 200)

    except (ValueError, FieldValidationError, ObjectValidationError) as e:
        return build_json_error_response(response, e, 400)
    except NotFoundValidationError as e:
        return build_json_error_response(response, e, 404)