import json
from django.http import JsonResponse
from products.models import Product, Brand
from products.serializers import serialize_product
from app.utils import get_json_from_request_body
from icecream import ic


def products_exception_to_json(exception):
    """
    Converts raw exception messages into user-friendly JSON error responses.
    """
    exception = str(exception)
    ERROR_MESSAGE_MAP = {
        "UNIQUE constraint failed: products_product.barcode": "Product with this barcode already exists",
        "Brand matching query does not exist.": "Brand with this id does not exist",
        "Product matching query does not exist.": "Product with this id does not exist",
        "'name'": "Invalid input. Field 'name' missing",
        "'brand'": "Invalid input. Field 'brand' missing",
        "'barcode'": "Invalid input. Field 'barcode' missing",
        "name 'brand' is not defined": "Field 'brand' invalid"
    }
    if exception in ERROR_MESSAGE_MAP:
        return {"error": ERROR_MESSAGE_MAP[exception]}
    return exception


def create_new_product(request, response):
    """
    Create (POST) new product based on request body
    """
    try:
        request_body = get_json_from_request_body(request)
        name = request_body['name']
        brand_id = request_body['brand']
        barcode = request_body['barcode']

        new_product = Product.objects.create(
            name=name,
            brand=Brand.objects.get(id=int(brand_id)),
            barcode=barcode
        )

        new_product.full_clean()
        new_product.save()
        
        response.append(serialize_product(new_product))
        return JsonResponse(response, safe=False, status=201)

    except Exception as e:
        response.append(products_exception_to_json(e))
        return JsonResponse(response, safe=False, status=400)


def get_product_detail(response, product_id):
    """
    GET a single product
    """
    try:
        product = Product.objects.get(id=product_id)
        response.append(serialize_product(product))
        return JsonResponse(response, safe=False, status=200)

    except Exception as e:
        response.append(products_exception_to_json(e))
        return JsonResponse(response, safe=False, status=400)


def update_product(request, response, product_id):
    """
    Use request body data given to UPDATE the product based on product_id given
    """
    try:
        request_body = get_json_from_request_body(request)
        product = Product.objects.get(id=product_id)
        product.name = request_body.get("name", product.name)
        product.barcode = request_body.get("barcode", product.barcode)
        product.brand = Brand.objects.get(id=int(request_body.get("brand", product.brand.pk)))
        product.save()

        response.append(serialize_product(product))
        return JsonResponse(response, safe=False, status=204)
    except Exception as e:
        response.append(products_exception_to_json(e))
        return JsonResponse(response, safe=False, status=400)


def delete_product(response, product_id):
    """
    DELETE product based on id given
    """
    try:
        product = Product.objects.get(id=product_id)
        product.delete()
        return JsonResponse(response, safe=False, status=204)
    except Exception as e:
        response.append(products_exception_to_json(e))
        return JsonResponse(response, safe=False, status=400)
