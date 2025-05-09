from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Store
from .utils import stores_exception_to_json
from app.utils import serialize_model_list, method_not_allowed
from stores.serializers import serialize_store
from stores.utils import (
    create_new_store,
    update_store,
    delete_store,
    get_store_detail
    )                                                                                            

@csrf_exempt
def store_create_list_view(request):
    response = []

    if request.method == "GET":
        return serialize_model_list(Store, stores_exception_to_json, serialize_store, response)

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
        return get_store_detail(response, store_id)

    if request.method == 'PUT':
        return update_store(request, response, store_id)

    if request.method == 'DELETE':
        return delete_store(response, store_id)

    return method_not_allowed(response)