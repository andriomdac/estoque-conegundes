from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from products.models import Product
from brands.models import Brand
from brands.serializers import serialize_brand
from brands.utils import (
    create_new_brand,
    update_brand,
    )
from app.utils.http import (
    method_not_allowed
    )
from app.utils.db_ops import (
    delete_model_object,
    serialize_model_list,
    get_model_object_detail,
)


@csrf_exempt
def brand_create_list_view(request):
    """
    GET list of brands or POST a new brand
    """
    response = []

    if request.method == 'GET':
        return serialize_model_list(response, Brand, serialize_brand)
    
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
        return get_model_object_detail(response, brand_id, Brand, serialize_brand, "brand")

    if request.method == 'PUT':
        return update_brand(request, response, brand_id)

    if request.method == 'DELETE':
        return delete_model_object(response, brand_id, Brand, "brand")
    return method_not_allowed(response)
