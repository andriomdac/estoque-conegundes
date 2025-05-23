from store_items.serializers import serialize_store_item

def serialize_sale_item(sale_item):
    """
    Transform a sale_item instance from a model to json
    """
    return {
        "id": sale_item.pk,
        "store_item": serialize_store_item(sale_item.store_item),
        "sale": sale_item.sale.pk,
        "created_at": sale_item.created_at,
        "updated_at": sale_item.updated_at
    }