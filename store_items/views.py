from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import StoreItem
from app.utils.db_ops import serialize_model_list, get_model_object_detail, delete_model_object
from app.utils.http import method_not_allowed
from .serializers import serialize_store_item
from store_items.utils import (
    create_new_store_item,
    update_store_item,
    )                                             
from tokens.decorators import token_required


@csrf_exempt
@token_required
def store_item_create_list_view(request):
    response = []

    if request.method == "GET":
        return serialize_model_list(response, StoreItem, serialize_store_item)

    if request.method == "POST":
        return create_new_store_item(request, response)


    return method_not_allowed(response)



@csrf_exempt
@token_required
def store_item_update_detail_delete_view(request, store_item_id):
    """
    GET, UPDATE or DELETE a store_item
    """
    response = []

    if request.method == 'GET':
        return get_model_object_detail(response, store_item_id, StoreItem, serialize_store_item, 'store item')

    if request.method == 'PUT':
        return update_store_item(request, response, store_item_id)

    if request.method == 'DELETE':
        return delete_model_object(response, store_item_id, StoreItem, 'store item')

    return method_not_allowed(response)