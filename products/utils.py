import json
from brands.models import Brand
from .models import Product
from .serializers import serialize_product
from .validators import validade_barcode
from app.utils.validators import (
    validate_request_body,
    validate_model_object_id,
    validate_and_save_model_object,
    validate_model_object_unique_name,
    )
from app.utils.http import (
    build_json_response,
    build_json_error_response,
    bad_request
    )
from app.utils.exceptions import (
    FieldValidationError,
    NotFoundValidationError,
    ObjectValidationError
    )


def create_new_product(request, response):
    try:
        data = validate_request_body(request=request, required_fields=["name", "brand", "barcode"])

        brand = validate_model_object_id(data['brand'], Brand, 'brand')
        barcode = validade_barcode(data['barcode'])
        name = validate_model_object_unique_name(data['name'], Product, 'product')
        
        new_product = validate_and_save_model_object(
            Product(
                name=name,
                brand=brand,
                barcode=barcode
            )
        )
        return build_json_response(response, serialize_product(new_product), 201)
    except (ValueError, FieldValidationError, ObjectValidationError) as e:
        return build_json_error_response(response, e, 400)
    except NotFoundValidationError as e:
        return build_json_error_response(response, e, 404)


def update_product(request, response, product_id):
    """
    Use request body data given to UPDATE the product based on product_id given
    """
    try:
        data = validate_request_body(request=request, required_fields=[])
        product = validate_model_object_id(product_id, Product, 'product')

        if 'name' in data:
            name = validate_model_object_unique_name(data['name'], Product, 'product')
            product.name = name
        if 'brand' in data:
            brand = validate_model_object_id(data['brand'], Brand, 'brand')
            product.brand = brand
        if 'barcode' in data:
            barcode = validade_barcode(data['barcode'])
            product.barcode = barcode
        
        product = validate_and_save_model_object(product)
        return build_json_response(response, serialize_product(product), 200)

    except (ValueError, FieldValidationError, ObjectValidationError) as e:
        return build_json_error_response(response=response, message=e, status=400)
    except NotFoundValidationError as e:
        return build_json_error_response(response, e, 404)