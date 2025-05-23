from app.utils.http import get_json_from_request_body, build_json_error_response, build_json_response
from app.utils.validators import validate_request_body
from django.core.validators import ValidationError
from .models import SaleItem
from store_items.models import StoreItem
from sales.models import Sale
from sale_items.serializers import serialize_sale_item
from store_items.validators import validate_store_item_id
from sales.validators import validate_sale_id


def create_new_sale_item(request, response):
    """
    Create (POST) new sale_item based on request body
    """
    try:
        data = validate_request_body(request, required_fields=["store_item", "sale"])
    except ValueError as e:
        return build_json_error_response(response, e, 400)

    try:
        store_item = validate_store_item_id(data['store_item'])
    except ValueError as e:
        return build_json_error_response(response, e, 400)
    except StoreItem.DoesNotExist as e:
        return build_json_error_response(response, e, 404)

    try:
        sale = validate_sale_id(data['sale'])
    except ValueError as e:
        return build_json_error_response(response, e, 400)
    except Sale.DoesNotExist as e:
        return build_json_error_response(response, e, 404)

    try:
        new_sale_item = SaleItem(
            store_item=store_item,
            sale=sale
        )
        new_sale_item.full_clean()
        new_sale_item.save()
    
    except ValidationError as e:
        return build_json_error_response(response, e, 400)

    return build_json_response(response, serialize_sale_item(new_sale_item), 201)