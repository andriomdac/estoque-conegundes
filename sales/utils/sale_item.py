import json
from django.http import JsonResponse
from sales.models import SaleItem, Sale
from stores.models import StoreItem
from sales.serializers import serialize_sale_item
from app.utils import get_json_from_request_body
from icecream import ic


def sale_items_exception_to_json(exception):
    """
    Converts raw exception messages into user-friendly JSON error responses.
    """
    exception = str(exception)
    ERROR_MESSAGE_MAP = {}
    if exception in ERROR_MESSAGE_MAP:
        return {"error": ERROR_MESSAGE_MAP[exception]}
    return exception


def create_new_sale_item(request, response):
    """
    Create (POST) new sale_item based on request body
    """
    try:
        request_body = get_json_from_request_body(request)
        store_item = StoreItem.objects.get(id=int(request_body['store_item']))
        sale = Sale.objects.get(id=int(request_body['sale']))

        new_sale_item = SaleItem.objects.create(
            store_item=store_item,
            sale=sale
        )

        new_sale_item.full_clean()
        new_sale_item.save()
        
        response.append(serialize_sale_item(new_sale_item))
        return JsonResponse(response, safe=False, status=201)

    except Exception as e:
        response.append(sale_items_exception_to_json(e))
        return JsonResponse(response, safe=False, status=400)


def get_sale_item_detail(response, sale_item_id):
    """
    GET a single sale_item
    """
    try:
        sale_item = SaleItem.objects.get(id=sale_item_id)
        response.append(serialize_sale_item(sale_item))
        return JsonResponse(response, safe=False, status=200)

    except Exception as e:
        response.append(sale_items_exception_to_json(e))
        return JsonResponse(response, safe=False, status=400)


def update_sale_item(request, response, sale_item_id):
    """
    Use request body data given to UPDATE the sale_item based on sale_item_id given
    """
    try:
        request_body = get_json_from_request_body(request)
        sale_item = SaleItem.objects.get(id=sale_item_id)
        sale_item.name = request_body.get("name", sale_item.name)
        sale_item.barcode = request_body.get("barcode", sale_item.barcode)
        sale_item.brand = Brand.objects.get(id=int(request_body.get("brand", sale_item.brand.pk)))
        sale_item.save()

        response.append(serialize_sale_item(sale_item))
        return JsonResponse(response, safe=False, status=204)
    except Exception as e:
        response.append(sale_items_exception_to_json(e))
        return JsonResponse(response, safe=False, status=400)


def delete_sale_item(response, sale_item_id):
    """
    DELETE sale_item based on id given
    """
    try:
        sale_item = SaleItem.objects.get(id=sale_item_id)
        sale_item.delete()
        return JsonResponse(response, safe=False, status=204)
    except Exception as e:
        response.append(sale_items_exception_to_json(e))
        return JsonResponse(response, safe=False, status=400)
