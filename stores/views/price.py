from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from stores.models import Store, StoreItemPrice
from app.utils import serialize_model_list, method_not_allowed
from stores.serializers import serialize_price
from stores.utils.price import (
    prices_exception_to_json,
    create_new_price,
    delete_price,
    get_price_detail
    )                                                                                            

@csrf_exempt
def price_create_list_view(request):
    response = []

    if request.method == "GET":
        return serialize_model_list(StoreItemPrice, prices_exception_to_json, serialize_price, response)

    if request.method == "POST":
        return create_new_price(request, response)


    return method_not_allowed(response)



@csrf_exempt
def price_detail_delete_view(request, price_id):
    """
    GET, UPDATE or DELETE a price
    """
    response = []

    if request.method == 'GET':
        return get_price_detail(response, price_id)

    if request.method == 'DELETE':
        return delete_price(response, price_id)

    return method_not_allowed(response)