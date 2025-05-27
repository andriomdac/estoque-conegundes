
def serialize_payment_method(payment_method, exclude_fields=[]):
    """
    Transform a sale_item instance from a model to json
    """
    data = {
        "id": payment_method.pk,
        "method": serialize_payment_method_choice(payment_method.method),
        "sale": payment_method.sale.pk,
        "total_amount": payment_method.total_amount,
    }
    if exclude_fields:
        for field in exclude_fields:
            del data[field]
    return data


def serialize_payment_method_choice(payment_method_choice):
    """
    Transform a payment_method_choice instance from a model to json
    """
    return {
        "id": payment_method_choice.pk,
        "name": payment_method_choice.name
    }