from app.utils.http import build_json_response, build_json_error_response
from .models import StoreItemPrice
from store_items.models import StoreItem
from .serializers import serialize_price
from app.utils.validators import (
    validate_request_body,
    validate_model_object_id,
    validate_monetary_value_field,
    validate_and_save_model_object,
    )
from app.utils.exceptions import (
    FieldValidationError,
    NotFoundValidationError,
    ObjectValidationError
    )


def create_new_price(request, response):
    """
    Create (POST) new price based on request body
    """
    try:
        data = validate_request_body(
            request,
            required_fields=[
                "store_item",
                "cost_price",
                "selling_price"
            ]
            )

        store_item = validate_model_object_id(data['store_item'], StoreItem, 'store_item')
        cost_price = validate_monetary_value_field(data['cost_price'], 'cost_price')
        selling_price = validate_monetary_value_field(data['selling_price'], 'selling_price')

        new_price = validate_and_save_model_object(
            StoreItemPrice(
            store_item=store_item,
            cost_price=cost_price,
            selling_price=selling_price
            )   
        )
        return build_json_response(response, serialize_price(new_price), 201 )

    except (ValueError, FieldValidationError, ObjectValidationError) as e:
        return build_json_error_response(response, e, 400)
    except NotFoundValidationError as e:
        return build_json_error_response(response, e, 404)
