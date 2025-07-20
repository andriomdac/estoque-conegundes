from app.utils.validators import validate_request_body
from app.utils.db_ops import delete_model_object
from app.utils.http import build_json_error_response, build_json_response
from .models import PaymentMethodValue, PaymentMethodChoice
from .serializers import serialize_payment_method
from sales.utils import update_sale_total_amount 
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
        
        # Update the sale total amount when a payment is successfuly deleted
        update_sale_total_amount(sale)
        return build_json_response(response, serialize_payment_method(new_payment), 201)

    except (ValueError, FieldValidationError, ObjectValidationError) as e:
        return build_json_error_response(response, e, 400)
    except NotFoundValidationError as e:
        return build_json_error_response(response, e, 404)


def delete_payment_method_value(response, payment_method_id, model_class, model_name):
        try:
            payment_method_value = validate_model_object_id(
                payment_method_id,
                PaymentMethodValue,
                'payment_method'
                )
            sale = PaymentMethodValue.objects.get(id=payment_method_id).sale

            delete_payment_response = delete_model_object(
                response,
                payment_method_id,
                model_class,
                model_name
                )
            
            # Update the sale total amount when a payment is successfuly deleted
            if delete_payment_response.status_code == 204:
                update_sale_total_amount(sale)

            return delete_payment_response
        except (FieldValidationError, NotFoundValidationError) as e:
            return build_json_error_response(response, e, 400)