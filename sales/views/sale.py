from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from sales.models import Sale
from sales.serializers import serialize_sale
from sales.utils.sale import (
    create_new_sale,
    get_sale_detail,
    update_sale,
    delete_sale,
    )
from app.utils import (
    get_json_from_request_body,
    serialize_model_list,
    method_not_allowed
    )


@csrf_exempt
def sale_create_list_view(request):
    """
    GET list of sales or POST a new sale
    """
    response = []

    if request.method == 'GET':
        return serialize_model_list(Sale, serialize_sale, response)
    
    if request.method == 'POST':
        return create_new_sale(request, response)

    return method_not_allowed(response)


@csrf_exempt
def sale_detail_delete_view(request, sale_id):
    """
    GET, UPDATE or DELETE a sale
    """
    response = []

    if request.method == 'GET':
        return get_sale_detail(response, sale_id)

    if request.method == 'DELETE':
        return delete_sale(response, sale_id)

    return method_not_allowed(response)
