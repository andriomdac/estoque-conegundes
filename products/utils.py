import json
from django.http import JsonResponse
from products.models import Product
from brands.models import Brand
from products.serializers import serialize_product
from app.utils.validators import validate_request_body
from products.validators import validade_barcode, validate_product_name
from brands.validators import validate_brand
from app.utils.exceptions import DuplicateBarcodeException
from icecream import ic
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from app.utils.exceptions import DuplicateProductException
from app.utils.http import (
    get_json_from_request_body,
    build_json_response,
    build_json_error_response,
    bad_request
    )


def create_new_product(request, response):
    try:
        data = validate_request_body(request=request, required_fields=["name", "brand", "barcode"])
    except ValueError as e:
        return build_json_error_response(response=response, message=e, status=400)

    try:
        brand = validate_brand(data['brand'])
    except ValueError as e:
        return build_json_error_response(response, e, status=400)
    except Brand.DoesNotExist as e:
        return build_json_error_response(response, e, status=404)

    try:
        barcode = validade_barcode(data['barcode'])
    except ValueError as e:
        return build_json_error_response(response, e, status=400)

    try:
        name = validate_product_name(data['name'], brand)
    except ValueError as e:
        return build_json_error_response(response, e, status=400)
    except DuplicateProductException as e:
        return build_json_error_response(response, e, status=400)

    try:
        new_product = Product.objects.create(
            name=name,
            brand=brand,
            barcode=barcode
        )

        new_product.full_clean()
        new_product.save()
        return build_json_response(response, serialize_product(new_product), status=201)

    except ValidationError as e:
        return build_json_error_response(response, e.message_dict, status=400)


def update_product(request, response, product_id):
    """
    Use request body data given to UPDATE the product based on product_id given
    """
    try:
        data = validate_request_body(request=request, required_fields=[])
    except ValueError as e:
        return build_json_error_response(response=response, message=e, status=400)

    brand = data.get('brand')
    barcode = data.get('barcode')
    name = data.get('name')

    try:
        product = Product.objects.get(id=product_id)
    except (ValueError, TypeError) as e:
        build_json_error_response(response, e, status=400)
    except Product.DoesNotExist as e:
        build_json_error_response(response, e, status=404)


    if 'brand' in data:
        try:
            brand = validate_brand(brand)
        except ValueError as e:
            return build_json_error_response(response, e, status=400)
        except Brand.DoesNotExist as e:
            return build_json_error_response(response, e, status=404)
    
    if 'barcode' in data:
        try:
            barcode = validade_barcode(barcode)
        except ValueError as e:
            return build_json_error_response(response, e, status=400)


    if 'name' in data:
        try:
            name = validate_product_name(name, brand)
        except ValueError as e:
            return build_json_error_response(response, e, status=400)
        except DuplicateProductException as e:
            return build_json_error_response(response, e, status=400)

    product.name = name or product.name
    product.brand = brand or product.brand
    product.barcode = barcode or product.barcode

    try:
        product.full_clean()
        product.save()
        return build_json_response(response)
    except ValidationError as e:
        return build_json_error_response(response, e.message_dict, status=400)
