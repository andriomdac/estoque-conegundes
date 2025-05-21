from store_items.models import StoreItem


def validate_store_item(store_item):
    if StoreItem.objects.filter(store=store_item.store, product=store_item.product).exists():
        raise ValueError(f"store '{store_item.store.pk}' already has this product '{store_item.product.pk}'")
    return store_item
from icecream import ic


def validate_store_item_id(store_item_id):
    try:
        store_item_id = int(store_item_id)
        store_item  = StoreItem.objects.get(id=store_item_id)
    except( TypeError, ValueError):
        raise ValueError("store item (ID) must be an integer.")
    except StoreItem.DoesNotExist:
        raise StoreItem.DoesNotExist(f"store item '{store_item_id}' does not exist.'")
    return store_item