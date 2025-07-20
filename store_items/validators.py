from store_items.models import StoreItem
from app.utils.validators import validate_and_save_model_object
from app.utils.http import build_json_error_response, build_json_response
from app.utils.exceptions import FieldValidationError


def validate_and_save_store_item(store_item):  
    if StoreItem.objects.filter(store=store_item.store, product=store_item.product).exists():
        raise FieldValidationError(
            f"store '{store_item.store.pk}' already have the product '{store_item.product.pk}'."
        )
    return validate_and_save_model_object(store_item)
