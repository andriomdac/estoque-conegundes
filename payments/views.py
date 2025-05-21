from django.views.decorators.csrf import csrf_exempt
from app.utils.db_ops import serialize_model_list, get_model_object_detail, delete_model_object
from .models import PaymentMethodValue
from .serializers import serialize_payment_method
from .utils import create_new_payment_method_value


@csrf_exempt
def payment_method_value_create_list_view(request):
    """
    GET list of payment_methods or POST a new payment_method
    """
    response = []

    if request.method == 'GET':
        return serialize_model_list(response, PaymentMethodValue, serialize_payment_method)
    
    if request.method == 'POST':
        return create_new_payment_method_value(request, response)

    return method_not_allowed(response)


@csrf_exempt
def payment_method_value_detail_delete_view(request, payment_method_id):
    """
    GET, UPDATE or DELETE a payment_method
    """
    response = []

    if request.method == 'GET':
        return get_model_object_detail(response, payment_method_id, PaymentMethodValue, serialize_payment_method, 'payment method')

    if request.method == 'DELETE':
        return delete_model_object(response, payment_method_id, PaymentMethodValue, 'payment method')

    return method_not_allowed(response)
    
