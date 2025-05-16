from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from sales.models import SaleItem
from sales.serializers import serialize_sale_item
from sales.utils.sale_item import (
    sale_items_exception_to_json,
    create_new_sale_item,
    get_sale_item_detail,
    update_sale_item,
    delete_sale_item,
    )
from app.utils import (
    get_json_from_request_body,
    serialize_model_list,
    method_not_allowed
    )


@csrf_exempt
def sale_item_create_list_view(request):
    """
    GET list of sale_items or POST a new sale_item
    """
    response = []

    if request.method == 'GET':
        return serialize_model_list(SaleItem, sale_items_exception_to_json, serialize_sale_item, response)
    
    if request.method == 'POST':
        return create_new_sale_item(request, response)

    return method_not_allowed(response)


@csrf_exempt
def sale_item_update_detail_delete_view(request, sale_item_id):
    """
    GET, UPDATE or DELETE a sale_item
    """
    response = []

    if request.method == 'GET':
        return get_sale_item_detail(response, sale_item_id)

    if request.method == 'PUT':
        return update_sale_item(request, response, sale_item_id)

    if request.method == 'DELETE':
        return delete_sale_item(response, sale_item_id)

    return method_not_allowed(response)
