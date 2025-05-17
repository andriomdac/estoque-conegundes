from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Store
from app.utils.db_ops import serialize_model_list, get_model_object_detail, delete_model_object
from app.utils.http import method_not_allowed
from .serializers import serialize_store
from .utils import (
    create_new_store,
    update_store,
    )                                                                                            


@csrf_exempt
def store_create_list_view(request):
    response = []

    if request.method == "GET":
        return serialize_model_list(response, Store, serialize_store)

    if request.method == "POST":
        return create_new_store(request, response)


    return method_not_allowed(response)


@csrf_exempt
def store_update_detail_delete_view(request, store_id):
    """
    GET, UPDATE or DELETE a store
    """
    response = []

    if request.method == 'GET':
        return get_model_object_detail(response, store_id, Store, serialize_store, 'store')

    if request.method == 'PUT':
        return update_store(request, response, store_id)

    if request.method == 'DELETE':
        return delete_model_object(response, store_id, Store, 'store')

    return method_not_allowed(response)