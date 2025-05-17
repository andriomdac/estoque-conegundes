def serialize_price(price):
    """
    Convert a Store instance to a JSON-serializable dict.
    """
    return {
        "id": price.pk,
        "store_item": price.store_item.pk,
        "cost_price": price.cost_price,
        "selling_price": price.selling_price,
        "created_at": price.created_at,
        "updated_at": price.updated_at,
        "active": price.active,
    }