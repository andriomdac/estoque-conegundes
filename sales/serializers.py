def serialize_sale(sale):
    """
    Transform a sale instance from a model to json
    """
    return {
        "id": sale.pk,
        "sale_items": {},
        "total_amount": sale.total_amount,
        "created_at": sale.created_at,
        "updated_at": sale.updated_at
    }
