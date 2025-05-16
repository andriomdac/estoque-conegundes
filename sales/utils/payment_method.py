import json
from django.http import JsonResponse
from sales.models import PaymentMethodValue, PaymentMethodChoice, Sale
from sales.serializers import serialize_payment_method
from app.utils import get_json_from_request_body
from icecream import ic


def payment_methods_exception_to_json(exception):
    """
    Converts raw exception messages into user-friendly JSON error responses.
    """
    exception = str(exception)
    ERROR_MESSAGE_MAP = {}
    if exception in ERROR_MESSAGE_MAP:
        return {"error": ERROR_MESSAGE_MAP[exception]}
    return exception


def create_new_payment_method(request, response):
    """
    Create (POST) new payment_method based on request body
    """
    try:
        request_body = get_json_from_request_body(request)

        method = PaymentMethodChoice.objects.get(id=request_body['method'])
        sale = Sale.objects.get(id=request_body['sale'])
        total_amount = request_body['total_amount']
        new_payment_method = PaymentMethodValue.objects.create(
            method=method,
            sale=sale,
            total_amount=total_amount
        )

        new_payment_method.full_clean()
        new_payment_method.save()
        
        response.append(serialize_payment_method(new_payment_method))
        return JsonResponse(response, safe=False, status=201)

    except Exception as e:
        response.append(payment_methods_exception_to_json(e))
        return JsonResponse(response, safe=False, status=400)


def get_payment_method_detail(response, payment_method_id):
    """
    GET a single payment_method
    """
    try:
        payment_method = PaymentMethodValue.objects.get(id=payment_method_id)
        response.append(serialize_payment_method(payment_method))
        return JsonResponse(response, safe=False, status=200)

    except Exception as e:
        response.append(payment_methods_exception_to_json(e))
        return JsonResponse(response, safe=False, status=400)


def delete_payment_method(response, payment_method_id):
    """
    DELETE payment_method based on id given
    """
    try:
        payment_method = PaymentMethodValue.objects.get(id=payment_method_id)
        payment_method.delete()
        return JsonResponse(response, safe=False, status=204)
    except Exception as e:
        response.append(payment_methods_exception_to_json(e))
        return JsonResponse(response, safe=False, status=400)