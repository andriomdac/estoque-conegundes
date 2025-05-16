import json
from django.http import JsonResponse
from stores.models import StoreItem, StoreCategory, Store
from products.models import Product
from stores.serializers import serialize_store_item
from app.utils import get_json_from_request_body


def store_item_exists_in_store(product, store):
    return StoreItem.objects.filter(store=store, product=product).exists()


def store_items_exception_to_json(exception):
    """
    Converts raw exception messages into user-friendly JSON error responses.
    """
    exception = str(exception)

    ERROR_MESSAGE_MAP = {
        "'store'": "Field 'store' required",
        "'category'": "Field 'category' required",
        "Field 'id' expected a number but got 'loja aberta'.": "'category' field must be an id (int)"
    }

    if exception in ERROR_MESSAGE_MAP:
        return {"error": ERROR_MESSAGE_MAP[exception]}

    return exception


def create_new_store_item(request, response):
    """
    Create (POST) new store_item based on request body
    """
    try:
        request_body = get_json_from_request_body(request)

        store = Store.objects.get(id=request_body['store'])
        category = StoreCategory.objects.get(id=request_body['category']) 
        product = Product.objects.get(id=request_body['product'])

        if not store_item_exists_in_store(product, store):
            new_store_item = StoreItem.objects.create(
                store=store,
                category=category,
                product=product,
            )
            new_store_item.full_clean()
            new_store_item.save()
            response.append(serialize_store_item(new_store_item))

            return JsonResponse(response, safe=False, status=201)
        else:
            response.append({"Error": f"Product {product.name}({product.pk}) already exist in store {store.name}({store.pk})"})
            return JsonResponse(response, safe=False, status=400)

    except Exception as e:
        response.append(store_items_exception_to_json(e))
        return JsonResponse(response, safe=False, status=400)


def get_store_item_detail(response, store_item_id):
    """
    GET a single store_item
    """
    try:
        store_item = StoreItem.objects.get(id=store_item_id)
        response.append(serialize_store_item(store_item))
        return JsonResponse(response, safe=False, status=200)

    except Exception as e:
        response.append(store_items_exception_to_json(e))
        return JsonResponse(response, safe=False, status=400)


def update_store_item(request, response, store_item_id):
    """
    Use request body data given to UPDATE the store_item based on store_item_id given
    """
    try:
        request_body = get_json_from_request_body(request)
        category_id = request_body['category']

        store_item = StoreItem.objects.get(id=store_item_id)
        store_item.category = StoreCategory.objects.get(id=category_id)
        store_item.save()

        response.append(serialize_store_item(store_item))
        return JsonResponse(response, safe=False, status=204)
    except Exception as e:
        response.append(store_items_exception_to_json(e))
        return JsonResponse(response, safe=False, status=400)


def delete_store_item(response, store_item_id):
    """
    DELETE store_item based on id given
    """
    try:
        store_item = StoreItem.objects.get(id=store_item_id)
        store_item.delete()
        return JsonResponse(response, safe=False, status=204)
    except Exception as e:
        response.append(store_items_exception_to_json(e))
        return JsonResponse(response, safe=False, status=400)
