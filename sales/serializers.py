from sale_items.serializers import serialize_sale_item, serialize_basic_sale_item
from payments.serializers import serialize_payment_method


def serialize_sale(sale):
    """
    Transform a sale instance from a model to json
    """
    return {
        "id": sale.pk,
        "active": sale.active,
        "total_amount": sale.total_amount,
        "created_at": sale.created_at,
        "updated_at": sale.updated_at,
        "payments":  [serialize_payment_method(method) for method in sale.payment_methods.all() ],
        "sale_items": [serialize_sale_item(sale_item) for sale_item in sale.sale_items.all()]
    }


def serialize_basic_sale(sale):
    """
    Transform a sale instance from a model to json, containing only the main (basic) info.
    """
    payments = {}
    payments_sum = 0
    for payment in sale.payment_methods.all():
        payments_sum += payment.total_amount
        payments[payment.method.name] = payment.total_amount

    return {
        "id": sale.pk,
        "total_amount": sale.total_amount,
        "created_at": sale.created_at,
        "updated_at": sale.updated_at,
        "payments": payments,
        "sale_items": sale.sale_items.all().count()

    }