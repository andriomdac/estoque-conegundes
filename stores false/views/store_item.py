from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from stores.models import StoreItem
from app.utils import serialize_model_list, method_not_allowed
from stores.serializers import serialize_store_item
from stores.utils.store_item import (
    store_items_exception_to_json,
    create_new_store_item,
    update_store_item,
    delete_store_item,
    get_store_item_detail
    )                                             


@csrf_exempt
def store_item_create_list_view(request):
    response = []

    if request.method == "GET":
        return serialize_model_list(StoreItem, store_items_exception_to_json, serialize_store_item, response)

    if request.method == "POST":
        return create_new_store_item(request, response)


    return method_not_allowed(response)



@csrf_exempt
def store_item_update_detail_delete_view(request, store_item_id):
    """
    GET, UPDATE or DELETE a store_item
    """
    response = []

    if request.method == 'GET':
        return get_store_item_detail(response, store_item_id)

    if request.method == 'PUT':
        return update_store_item(request, response, store_item_id)

    if request.method == 'DELETE':
        return delete_store_item(response, store_item_id)

    return method_not_allowed(response)