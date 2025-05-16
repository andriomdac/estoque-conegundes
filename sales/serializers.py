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


def serialize_sale_item(sale_item):
    """
    Transform a sale_item instance from a model to json
    """
    return {
        "id": sale_item.pk,
        "store_item": sale_item.store_item.pk,
        "sale": sale_item.sale.pk,
        "created_at": sale_item.created_at,
        "updated_at": sale_item.updated_at
    }


def serialize_payment_method(payment_method):
    """
    Transform a sale_item instance from a model to json
    """
    return {
        "id": payment_method.pk,
        "method": payment_method.method.pk,
        "sale": payment_method.sale.pk,
        "total_amount": payment_method.total_amount,
    }

def serialize_payment_method_choice(payment_method_choice):
    """
    Transform a payment_method_choice instance from a model to json
    """
    return {
        "id": payment_method_choice.pk,
        "name": payment_method_choice.name
    }