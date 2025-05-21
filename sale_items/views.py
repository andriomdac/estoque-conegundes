from django.views.decorators.csrf import csrf_exempt
from app.utils.db_ops import serialize_model_list, get_model_object_detail, delete_model_object
from .models import SaleItem
from .serializers import serialize_sale_item
from app.utils.http import method_not_allowed
from .utils import create_new_sale_item


@csrf_exempt
def sale_item_create_list_view(request):
    """
    GET list of sale_items or POST a new sale_item
    """
    response = []

    if request.method == 'GET':
        return serialize_model_list(response, SaleItem, serialize_sale_item)
    
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
        return get_model_object_detail(response, sale_item_id, SaleItem, serialize_sale_item, 'sale_item')

    if request.method == 'PUT':
        pass

    if request.method == 'DELETE':
        return delete_model_object(response, sale_item_id, SaleItem, 'sale_item')

    return method_not_allowed(response)
