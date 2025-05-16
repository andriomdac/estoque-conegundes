import json
from django.http import JsonResponse
from .models import Category
from categories.serializers import serialize_category
from app.utils.http import (
    get_json_from_request_body,
    build_json_response,
    bad_request
    )
from app.utils.db_ops import serialize_model_list
from django.core.exceptions import ValidationError
from django.db.models.deletion import ProtectedError


def create_new_category(request, response):
    """
    Create (POST) new category based on request body
    """
    try:
        data = get_json_from_request_body(request)
    except json.JSONDecodeError:
        return build_json_response(response, {"error": "invalid request body"}, status=400)

    name = data.get('name')

    if name:
        new_category = Category.objects.create(
            name=name
        )
        new_category.full_clean()
        new_category.save()
        return build_json_response(response, serialize_category(new_category), status=201)

    return build_json_response(
        response,
        {
            "error": "Field 'name' invalid or missing.",
            "expected structure": {
                "name": "category_name"
                }},
        status=400)


def update_category(request, response, category_id):
    """
    Use request body data given to UPDATE the category based on category_id given
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
                    "name": "category_name"
                    }},
            status=400)

    try:
        category = Category.objects.get(id=category_id)
        category.name = new_name
        category.full_clean()
        category.save()
        return build_json_response(response, serialize_category(category), 200)

    except ValidationError as e:
        return build_json_response(response, {"error": e.message_dict}, status=400)
    except Category.DoesNotExist:
        return build_json_response(response, {"error": "Category not found."}, status=404)