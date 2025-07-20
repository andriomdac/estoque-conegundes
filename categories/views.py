from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from products.models import Product
from categories.models import Category
from categories.serializers import serialize_category
from categories.utils import (
    create_new_category,
    update_category,
    )
from app.utils.http import (
    method_not_allowed
    )
from app.utils.db_ops import (
    delete_model_object,
    serialize_model_list,
    get_model_object_detail,
)
from tokens.decorators import token_required


@csrf_exempt
@token_required
def category_create_list_view(request):
    """
    GET list of categories or POST a new category
    """
    response = []

    if request.method == 'GET':
        return serialize_model_list(response, Category, serialize_category)
    
    if request.method == 'POST':
        return create_new_category(request, response)

    return method_not_allowed(response)


@csrf_exempt
@token_required
def category_update_detail_delete_view(request, category_id):
    """
    GET, UPDATE or DELETE a category
    """
    response = []

    if request.method == 'GET':
        return get_model_object_detail(response, category_id, Category, serialize_category, "category")

    if request.method == 'PUT':
        return update_category(request, response, category_id)

    if request.method == 'DELETE':
        return delete_model_object(response, category_id, Category, "category")
    return method_not_allowed(response)
