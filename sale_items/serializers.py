from store_items.serializers import serialize_store_item

def serialize_sale_item(sale_item, exclude_fields=[]):
    """
    Transform a sale_item instance from a model to json
    """
    data = {
        "id": sale_item.pk,
        "store_item": serialize_store_item(sale_item.store_item),
        "sale": sale_item.sale.pk,
        "created_at": sale_item.created_at,
        "updated_at": sale_item.updated_at
    }
    if exclude_fields:
        for field in exclude_fields:
            del data[field]
    return data


def serialize_basic_sale_item(sale_item, exclude_fields=[]):
    """
    Transform a sale_item instance from a model to json
    """
    data = {
        "id": sale_item.pk,
        "store_item": serialize_store_item(sale_item.store_item, exclude_fields=["created_at", "updated_at", "active"]),
        "sale": sale_item.sale.pk,
    }
    if exclude_fields:
        for field in exclude_fields:
            del data[field]
    return data