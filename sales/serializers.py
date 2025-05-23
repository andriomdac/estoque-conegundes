from sale_items.serializers import serialize_sale_item

def serialize_sale(sale):
    """
    Transform a sale instance from a model to json
    """
    return {
        "id": sale.pk,
        "sale_items": [serialize_sale_item(sale_item) for sale_item in sale.sale_items.all()],
        "total_amount": sale.total_amount,
        "created_at": sale.created_at,
        "updated_at": sale.updated_at
    }
