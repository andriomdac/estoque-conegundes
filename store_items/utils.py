import json
from .models import StoreItem
from products.models import Product
from categories.models import Category
from stores.models import Store
from .serializers import serialize_store_item
from app.utils.http import build_json_error_response, build_json_response
from app.utils.validators import (
    validate_request_body,
    validate_and_save_model_object,
    validate_model_object_id
    )
from app.utils.exceptions import (
    FieldValidationError,
    NotFoundValidationError,
    ObjectValidationError
    )
from .validators import validate_and_save_store_item


def create_new_store_item(request, response):
    try:
        data = validate_request_body(request=request, required_fields=["store", "product", "category"])

        store = validate_model_object_id(data['store'], Store, 'store')
        product = validate_model_object_id(data['product'], Product, 'product')
        category = validate_model_object_id(data['category'], Category, 'category')
        
        new_store_item = validate_and_save_store_item(
            StoreItem(
                store=store,
                product=product,
                category=category
            )
        )
        return build_json_response(response, serialize_store_item(new_store_item), 201)
    except (ValueError, FieldValidationError, ObjectValidationError) as e:
        return build_json_error_response(response, e, 400)
    except NotFoundValidationError as e:
        return build_json_error_response(response, e, 404)


def update_store_item(request, response, store_item_id):
    """
    Use request body data given to UPDATE the product based on product_id given
    """
    try:
        data = validate_request_body(request=request, required_fields=[])
        store_item = validate_model_object_id(store_item_id, StoreItem, 'store_item')

        if 'category' in data:
            category = validate_model_object_id(data['category'], Category, 'category')
            store_item.category = category
        
        store_item = validate_and_save_model_object(store_item)
        return build_json_response(response, serialize_store_item(store_item), 200)

    except (ValueError, FieldValidationError, ObjectValidationError) as e:
        return build_json_error_response(response=response, message=e, status=400)
    except NotFoundValidationError as e:
        return build_json_error_response(response, e, 404)
