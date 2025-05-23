import json
#Models
from .models import StoreItem
from products.models import Product
from categories.models import Category
from stores.models import Store
#Serializers
from .serializers import serialize_store_item
#Responses
from app.utils.http import build_json_error_response, build_json_response
#Validators
from app.utils.validators import validate_request_body
from stores.validators import validate_store
from django.core.validators import ValidationError
from .validators import validate_store_item


def create_new_store_item(request, response):
    """
    Create (POST) new store_item based on request body
    """
    try:
        data = validate_request_body(
            request,
            required_fields=[
                "store",
                "product",
                "category",
                ]
            )
    except ValueError as e:
        return build_json_error_response(response, e, 400)
    
    try:
        store = validate_store(data['store'])
    except ValueError as e:
        return build_json_error_response(response, e, 400)

    try:
        product = validate_product(data['product'])
    except Product.DoesNotExist as e:
        return build_json_error_response(response, e, 404)
    except ValueError as e:
        return build_json_error_response(response, e, 400)

    try:
        category = validate_category(data['category'])
    except ValueError as e:
        return build_json_error_response(response, e, 400)
    except Category.DoesNotExist as e:
        return build_json_error_response(response, e, 404)

    try:
        new_store_item = validate_store_item(
            StoreItem(
                store=store,
                product=product,
                category=category
                )
            )
        new_store_item.full_clean()
        new_store_item.save()
        return build_json_response(response, serialize_store_item(new_store_item), 201)
    except ValidationError as e:
        return build_json_error_response(response, e, 400)
    except ValueError as e:
        return build_json_error_response(response, e, 400)
    


def update_store_item(request, response, store_item_id):
    """
    Use request body data given to UPDATE the store_item based on store_item_id given
    """
    try:
        data = validate_request_body(request)
    except ValueError as e:
        return build_json_error_response(response, e, 400)

    if 'category' in data:
        try:
            category = validate_category(data['category'])
        except (ValueError, TypeError) as e:
            return build_json_error_response(response, e, 400)
        except Category.DoesNotExist as e:
            return build_json_error_response(response, e, 404)

    try:
        store_item = StoreItem.objects.get(id=store_item_id)
        store_item.category = category if category else  store_item.category
        store_item.full_clean()
        store_item.save()
        return build_json_response(response, serialize_store_item(store_item), 200)
    except (ValidationError, ValueError) as e:
        return build_json_error_response(response, e, 400)
    except StoreItem.DoesNotExist as e:
        return build_json_error_response(response, e, 404)