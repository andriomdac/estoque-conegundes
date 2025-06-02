from django.views.decorators.csrf import csrf_exempt
from .models import StoreItemPrice
from app.utils.db_ops import serialize_model_list, get_model_object_detail, delete_model_object
from app.utils.http import method_not_allowed
from .serializers import serialize_price
from .utils import (
    create_new_price,
    )                                                                                    
from tokens.decorators import token_required


@csrf_exempt
@token_required
def price_create_list_view(request):
    response = []

    if request.method == "GET":
        return serialize_model_list(response, StoreItemPrice, serialize_price)

    if request.method == "POST":
        return create_new_price(request, response)

    return method_not_allowed(response)



@csrf_exempt
@token_required
def price_detail_delete_view(request, price_id):
    """
    GET, UPDATE or DELETE a price
    """
    response = []

    if request.method == 'GET':
        return get_model_object_detail(response, price_id, StoreItemPrice, serialize_price, 'price')

    if request.method == 'DELETE':
        return delete_model_object(response, price_id, StoreItemPrice, 'price')

    return method_not_allowed(response)