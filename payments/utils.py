from app.utils.validators import validate_request_body
from app.utils.http import build_json_error_response, build_json_response
from .models import PaymentMethodValue, PaymentMethodChoice
from .serializers import serialize_payment_method
from sales.models import Sale
from django.core.validators import ValidationError
from sales.validators import validate_sale_id, validate_total_amount
from payments.validators import validate_method_id


def create_new_payment_method_value(request, response):
    """
    Create (POST) new payment_method based on request body
    """
    try:
        data = validate_request_body(request, required_fields=["method", "sale", "total_amount"])
    except ValueError as e:
        return build_json_error_response(response, e, 400)

    try:
        method = validate_method_id(data['method'])
    except PaymentMethodChoice.DoesNotExist as e:
        return build_json_error_response(response, e, 404)
    except ValueError as e:
        return build_json_error_response(response, e, 400)

    try:
        sale = validate_sale_id(data['sale'])
    except Sale.DoesNotExist as e:
        return build_json_error_response(response, e, 404)
    except ValueError as e:
        return build_json_error_response(response, e, 400)

    try:
        total_amount = validate_total_amount(data['total_amount'])
    except ValueError as e:
        return build_json_error_response(response, e, 400)

    try:
        new_payment = PaymentMethodValue(
            method=method,
            sale=sale,
            total_amount=total_amount
        )
        new_payment.full_clean()
        new_payment.save()
    except ValidationError as e:
        return build_json_error_response(response, e, 400)

    return build_json_response(response, serialize_payment_method(new_payment), 201)