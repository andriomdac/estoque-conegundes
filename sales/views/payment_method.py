from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from sales.models import PaymentMethodValue, PaymentMethodChoice
from sales.serializers import serialize_payment_method, serialize_payment_method_choice
from sales.utils.payment_method import (
    payment_methods_exception_to_json,
    create_new_payment_method,
    get_payment_method_detail,
    delete_payment_method,
    )
from app.utils import (
    get_json_from_request_body,
    serialize_model_list,
    method_not_allowed
    )


@csrf_exempt
def payment_method_create_list_view(request):
    """
    GET list of payment_methods or POST a new payment_method
    """
    response = []

    if request.method == 'GET':
        return serialize_model_list(PaymentMethodValue, payment_methods_exception_to_json, serialize_payment_method, response)
    
    if request.method == 'POST':
        return create_new_payment_method(request, response)

    return method_not_allowed(response)


@csrf_exempt
def payment_method_detail_delete_view(request, payment_method_id):
    """
    GET, UPDATE or DELETE a payment_method
    """
    response = []

    if request.method == 'GET':
        return get_payment_method_detail(response, payment_method_id)

    if request.method == 'DELETE':
        return delete_payment_method(response, payment_method_id)

    return method_not_allowed(response)


def payment_method_choice_list_view(request):
    """
    GET list of payment_method choices
    """
    response = []

    if request.method == 'GET':
        choices = PaymentMethodChoice.objects.all()
        for choice in choices:
            response.append(serialize_payment_method_choice(choice))
        return JsonResponse(response, safe=False, status=200)
    return method_not_allowed(response)
    
