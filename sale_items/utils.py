from app.utils.http import get_json_from_request_body, build_json_error_response, build_json_response
from app.utils.validators import validate_request_body
from django.core.validators import ValidationError
from .models import SaleItem
from store_items.models import StoreItem
from sales.models import Sale
from sale_items.serializers import serialize_sale_item
from app.utils.validators import (
    validate_and_save_model_object,
    validate_model_object_id
    )
from app.utils.exceptions import (
    FieldValidationError,
    NotFoundValidationError,
    ObjectValidationError
    )

def create_new_sale_item(request, response):
    try:
        data = validate_request_body(request=request, required_fields=["store_item", "sale"])

        store_item = validate_model_object_id(data['store_item'], StoreItem, 'store_item')
        sale = validate_model_object_id(data['sale'], Sale, 'sale')
        
        new_sale_item = validate_and_save_model_object(
            SaleItem(
                store_item=store_item,
                sale=sale
            )
        )
        return build_json_response(response, serialize_sale_item(new_sale_item), 201)
    except (ValueError, FieldValidationError, ObjectValidationError) as e:
        return build_json_error_response(response, e, 400)
    except NotFoundValidationError as e:
        return build_json_error_response(response, e, 404)