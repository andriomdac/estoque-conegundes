import json
from django.http import JsonResponse
from .models import Category
from categories.serializers import serialize_category
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
from .validators import validate_category_name


def create_new_category(request, response):
    """
    Create (POST) new category based on request body
    """
    try:
        data = validate_request_body(request, required_fields=['name'])
    except ValueError as e:
        return build_json_error_response(response, e, 400)

    if 'name' in data:
        try:
            name = validate_category_name(data['name'])
        except ValueError as e:
            return build_json_error_response(response, e, 400)
    
    try:
        new_category = Category(name=name)
        new_category.full_clean()
        new_category.save()
        return build_json_response(response, serialize_category(new_category), 201)
    except ValidationError as e:
        return build_json_error_response(response, e, 400)
    except Category.DoesNotExist as e:
        return build_json_error_response(response, e, 404)



def update_category(request, response, category_id):
    """
    Use request body data given to UPDATE the category based on category_id given
    """
    try:
        data = validate_request_body(request)
    except ValueError as e:
        return build_json_error_response(response, e, status=400)

    if 'name' in data:
        try:
            name = validate_category_name(data['name'])
        except ValueError as e:
            return build_json_error_response(response, e, 400)
    
    try:
        category = Category.objects.get(id=category_id)
        category.name = name
        category.full_clean()
        category.save()
        return build_json_response(response, serialize_category(category), 200)

    except ValidationError as e:
        return build_json_error_response(response, e, 400)
    except Category.DoesNotExist as e:
        return build_json_error_response(response, e, 404)