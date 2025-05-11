from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from products.models import Product
from products.models import Brand
from products.serializers import serialize_product
from products.utils.product import (
    products_exception_to_json,
    create_new_product,
    get_product_detail,
    update_product,
    delete_product,
    )
from app.utils import (
    get_json_from_request_body,
    serialize_model_list,
    method_not_allowed
    )


@csrf_exempt
def product_create_list_view(request):
    """
    GET list of products or POST a new product
    """
    response = []

    if request.method == 'GET':
        return serialize_model_list(Product, products_exception_to_json, serialize_product, response)
    
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
        return get_product_detail(response, product_id)

    if request.method == 'PUT':
        return update_product(request, response, product_id)

    if request.method == 'DELETE':
        return delete_product(response, product_id)

    return method_not_allowed(response)
