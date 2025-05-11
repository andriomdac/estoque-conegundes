from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from products.models import Product, Brand
from products.models import Brand
from products.serializers import serialize_brand
from products.utils.brand import (
    brands_exception_to_json,
    create_new_brand,
    get_brand_detail,
    update_brand,
    delete_brand,
    )
from app.utils import (
    get_json_from_request_body,
    serialize_model_list,
    method_not_allowed
    )


@csrf_exempt
def brand_create_list_view(request):
    """
    GET list of brands or POST a new brand
    """
    response = []

    if request.method == 'GET':
        return serialize_model_list(Brand, brands_exception_to_json, serialize_brand, response)
    
    if request.method == 'POST':
        return create_new_brand(request, response)

    return method_not_allowed(response)


@csrf_exempt
def brand_update_detail_delete_view(request, brand_id):
    """
    GET, UPDATE or DELETE a brand
    """
    response = []

    if request.method == 'GET':
        return get_brand_detail(response, brand_id)

    if request.method == 'PUT':
        return update_brand(request, response, brand_id)

    if request.method == 'DELETE':
        return delete_brand(response, brand_id)

    return method_not_allowed(response)
