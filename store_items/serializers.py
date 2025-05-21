from products.serializers import serialize_product
from stores.serializers import serialize_store
from categories.serializers import serialize_category

def serialize_store_item(store_item):
    """
    Convert a StoreItem instance to a JSON-serializable dict.
    """
    return {
        "id": store_item.pk,
        "product": serialize_product(store_item.product),
        "store": serialize_store(store_item.store),
        "category": serialize_category(store_item.category),
        "quantity": store_item.quantity,
        "created_at": store_item.created_at,
        "updated_at": store_item.updated_at,
        "active": store_item.active,
    }