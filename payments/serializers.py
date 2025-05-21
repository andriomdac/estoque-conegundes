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