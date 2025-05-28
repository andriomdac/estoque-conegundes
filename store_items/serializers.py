from products.serializers import serialize_product
from stores.serializers import serialize_store
from categories.serializers import serialize_category
from icecream import ic

def serialize_store_item(store_item, exclude_fields=[]):
    """
    Convert a StoreItem instance to a JSON-serializable dict.
    """
    data = {
        "id": store_item.pk,
        "product": serialize_product(store_item.product),
        "selling_price": "no price",
        "store": serialize_store(store_item.store),
        "category": serialize_category(store_item.category),
        "quantity": store_item.quantity,
        "created_at": store_item.created_at,
        "updated_at": store_item.updated_at,
        "active": store_item.active,
    }

    # Get the latest store item price (the current price)
    prices = store_item.prices.all()
    if prices:
        current_store_item_price = prices.order_by("-created_at").first().selling_price
        data['selling_price'] = current_store_item_price
    if exclude_fields:
        for field in exclude_fields:
            del data[field]
    return data


def serialize_basic_store_item(store_item, exclude_fields=[]):
    """
    Convert a StoreItem instance to a JSON-serializable dict.
    """
    data = {
        "id": store_item.pk,
        "product": store_item.product.pk,
        "store": store_item.store.pk,
        "category": store_item.category.pk,
        "quantity": store_item.quantity
    }

    if exclude_fields:
        for field in exclude_fields:
            del data[field]
    return data