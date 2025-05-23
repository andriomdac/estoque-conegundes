from app.utils.validators import validate_request_body
from app.utils.http import build_json_error_response, build_json_response
from .models import PaymentMethodValue, PaymentMethodChoice
from .serializers import serialize_payment_method
from sales.models import Sale
from app.utils.validators import (
    validate_model_object_id,
    validate_monetary_value_field,
    validate_and_save_model_object
    )
from app.utils.exceptions import (
    FieldValidationError,
    NotFoundValidationError,
    ObjectValidationError
    )


def create_new_payment_method_value(request, response):
    """
    Create (POST) new payment_method based on request body
    """
    try:
        data = validate_request_body(request, required_fields=["method", "sale", "total_amount"])

        method = validate_model_object_id(data['method'], PaymentMethodChoice, 'method')
        sale = validate_model_object_id(data['sale'], Sale, 'sale')
        total_amount = validate_monetary_value_field(data['total_amount'], 'total_amount')

        new_payment = validate_and_save_model_object(
            object=PaymentMethodValue(
                method=method,
                sale=sale,
                total_amount=total_amount
                )
             )
        return build_json_response(response, serialize_payment_method(new_payment), 201)

    except (ValueError, FieldValidationError, ObjectValidationError) as e:
        return build_json_error_response(response, e, 400)
    except NotFoundValidationError as e:
        return build_json_error_response(response, e, 404)

