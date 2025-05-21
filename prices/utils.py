from app.utils.http import build_json_response, build_json_error_response
from app.utils.validators import validate_request_body
from .models import StoreItemPrice
from store_items.models import StoreItem
from .serializers import serialize_price
from store_items.validators import validate_store_item_id
from .validators import validate_cost_price, validate_selling_price, validate_store_item_price
from django.core.validators import ValidationError

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
    except ValueError as e:
        return build_json_error_response(response, e, 400)
    
    try:
        store_item = validate_store_item_id(data['store_item'])
    except ValueError as e:
        return build_json_error_response(response, e, 400)
    except StoreItem.DoesNotExist as e:
        return build_json_error_response(response, e, 404)

    try:
        cost_price = validate_cost_price(data['cost_price'])
    except ValueError as e:
        return build_json_error_response(response, e, 400)

    try:
        selling_price = validate_selling_price(data['selling_price'])
    except ValueError as e:
        return build_json_error_response(response, e, 400)

    try:
        new_price = validate_store_item_price(
            StoreItemPrice(
            store_item=store_item,
            cost_price=cost_price,
            selling_price=selling_price
            )   
        )
        new_price.full_clean()
        new_price.save()
    except ValueError as e:
        return build_json_error_response(response, e, 400)
    except ValidationError as e:
        return build_json_error_response(response, e.message_dict, 400)
    return build_json_response(response, serialize_price(new_price), 201 )
