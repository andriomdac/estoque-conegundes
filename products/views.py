from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from products.models import Product
from products.models import Brand
from products.serializers import serialize_product
from products.utils import (
    create_new_product,
    update_product,
    )
from app.utils.db_ops import (
    delete_model_object,
    serialize_model_list,
    get_model_object_detail,
    )
from app.utils.http import (
    get_json_from_request_body,
    method_not_allowed
)


@csrf_exempt
def product_create_list_view(request):
    """
    GET list of products or POST a new product
    """
    response = []

    if request.method == 'GET':
        return serialize_model_list(response, Product, serialize_product)
    
    if request.method == 'POST':
        return create_new_product(request, response)

    return method_not_allowed(response)


@csrf_exempt
def product_update_detail_delete_view(request, product_id):
    """
    GET, UPDATE or DELETE a product
    """
    response = []

    if request.method == 'GET':
        return get_model_object_detail(response, product_id, Product, serialize_product, "product")

    if request.method == 'PUT':
        return update_product(request, response, product_id)

    if request.method == 'DELETE':
        return delete_model_object(response, product_id, Product, "product")

    return method_not_allowed(response)
