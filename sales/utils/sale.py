import json
from django.http import JsonResponse
from sales.models import Sale
from sales.serializers import serialize_sale
from app.utils import (
    get_json_from_request_body,
    build_json_response,
    serialize_model_list,
    bad_request
)
from icecream import ic
from django.core.exceptions import ValidationError
from django.db.models.deletion import ProtectedError


def get_sales_list(response):
    """
    GET list of all sales
    """
    return serialize_model_list(Sale, serialize_sale, response)


def create_new_sale(request, response):
    """
    Create (POST) new sale based on request body
    """
    try:
        data = get_json_from_request_body(request)
    except json.JSONDecodeError:
        return build_json_response(response, {"error": "invalid request body"}, status=400)

    new_sale = Sale.objects.create()

    return build_json_response(response,serialize_sale(new_sale) ,status=201)


def get_sale_detail(response, sale_id):
    """
    GET a single sale
    """
    try:
        sale = Sale.objects.get(id=sale_id)
        return build_json_response(response, serialize_sale(sale), 200)
    except Sale.DoesNotExist:
        return build_json_response(response, {"error": f"Sale '{sale_id}' does not exist."}, status=404)


def update_sale(request, response, sale_id):
    """
    Use request body data given to UPDATE the sale based on sale_id given
    """
    try:
        data = get_json_from_request_body(request)
    except json.JSONDecodeError:
        return build_json_response(response, {"error": "invalid request body"}, status=400)

    try:
        sale = Sale.objects.get(id=sale_id)
        
        sale.full_clean()
        sale.save()
        return build_json_response(response, serialize_sale(sale), 200)

    except ValidationError as e:
        return build_json_response(response, {"error": e.message_dict}, status=400)
    except Sale.DoesNotExist:
        return build_json_response(response, {"error": "Sale not found."}, status=404)


def delete_sale(response, sale_id):
    """
    DELETE sale based on id given
    """
    try:
        sale = Sale.objects.get(id=sale_id)
        sale.delete()
        return JsonResponse({}, safe=False, status=204)
    except Sale.DoesNotExist:
        return build_json_response(response, {"error": "Sale not found"}, status=404)
    except ProtectedError:
        return build_json_response(response, {"error": "Cannot delete sale as it's referenced by other objects"}, status=400)
    except Exception as e:
        return build_json_response(response, {"error": str(e)}, status=400)