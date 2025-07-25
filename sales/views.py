from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Sale
from .serializers import serialize_sale, serialize_basic_sale
from .utils import create_new_sale, finalize_sale, activate_sale
from app.utils.db_ops import get_model_object_detail, delete_model_object, serialize_model_list
from app.utils.http import method_not_allowed
from tokens.decorators import token_required


@csrf_exempt
@token_required
def sale_create_list_view(request):
    """
    GET list of sales or POST a new sale
    """
    response = []

    if request.method == 'GET':
        return serialize_model_list(response, Sale, serialize_basic_sale)
    
    if request.method == 'POST':
        return create_new_sale(request, response)

    return method_not_allowed(response)


@csrf_exempt
@token_required
def sale_detail_delete_view(request, sale_id):
    """
    GET, UPDATE or DELETE a sale
    """
    response = []

    if request.method == 'GET':
        return get_model_object_detail(response, sale_id, Sale, serialize_sale, "sale")

    if request.method == 'DELETE':
        return delete_model_object(response, sale_id, Sale, "sale")

    return method_not_allowed(response)

from icecream import ic


@csrf_exempt
@token_required
def sale_activate_view(request, sale_id):
    response = []

    if request.method == 'POST':
        return activate_sale(response, sale_id)
    
    return method_not_allowed(response)


@csrf_exempt
@token_required
def sale_finalize_view(request, sale_id):
    response = []

    if request.method == 'POST':
        return finalize_sale(response, sale_id)
    
    return method_not_allowed(response)

