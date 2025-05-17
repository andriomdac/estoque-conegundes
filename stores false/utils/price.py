import json
from django.http import JsonResponse
from stores.models import Store, StoreItem, StoreItemPrice
from stores.serializers import serialize_price
from app.utils import get_json_from_request_body
from icecream import ic

def active_store_item_price_exists(store_item):
    return store_item.prices.filter(active=True).exists()

def prices_exception_to_json(exception):
    """
    Converts raw exception messages into user-friendly JSON error responses.
    """
    exception = str(exception)

    ERROR_MESSAGE_MAP = {}

    if exception in ERROR_MESSAGE_MAP:
        return {"error": ERROR_MESSAGE_MAP[exception]}

    return exception


def create_new_price(request, response):
    """
    Create (POST) new price based on request body
    """
    try:
        request_body = get_json_from_request_body(request)


        store_item = StoreItem.objects.get(id=request_body['store_item'])
        cost_price = request_body['cost_price']
        selling_price = request_body['selling_price']

        if not active_store_item_price_exists(store_item):
            new_price = StoreItemPrice.objects.create(
                store_item=store_item,
                cost_price=cost_price,
                selling_price=selling_price,   
            )

            new_price.full_clean()
            new_price.save()
        else:
            response.append({"Error": "There is an active price already being used by this store item"})
            return JsonResponse(response, safe=False, status=400)

        
        response.append(serialize_price(new_price))
        return JsonResponse(response, safe=False, status=201)

    except Exception as e:
        response.append(prices_exception_to_json(e))
        return JsonResponse(response, safe=False, status=400)


def get_price_detail(response, price_id):
    """
    GET a single price
    """
    try:
        price = StoreItemPrice.objects.get(id=price_id)
        response.append(serialize_price(price))
        return JsonResponse(response, safe=False, status=200)

    except Exception as e:
        response.append(prices_exception_to_json(e))
        return JsonResponse(response, safe=False, status=400)


def delete_price(response, price_id):
    """
    DELETE price based on id given
    """
    try:
        price = StoreItemPrice.objects.get(id=price_id)
        price.delete()
        return JsonResponse(response, safe=False, status=204)
    except Exception as e:
        response.append(prices_exception_to_json(e))
        return JsonResponse(response, safe=False, status=400)
