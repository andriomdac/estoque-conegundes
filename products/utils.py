def convert_product_instance_to_json(product):
    """
    Transform a product instance from a model to a json
    """
    return {
        "id": product.pk,
        "name": product.name,
        "brand": product.brand.name,
        "barcode": product.barcode,
    }

def exception_to_json(exception):
    """
    Converts raw exception messages into user-friendly JSON error responses.
    """
    import json


    exception = str(exception)

    ERROR_MESSAGE_MAP = {
        "UNIQUE constraint failed: products_product.barcode": "Product with this barcode already exists",
        "Brand matching query does not exist.": "Brand with this id does not exist",
        "Product matching query does not exist.": "Product with this id does not exist"
    }

    if exception in ERROR_MESSAGE_MAP:
        return {"error": ERROR_MESSAGE_MAP[exception]}

    return exception

def get_json_from_request_body(request):
    return json.loads(request.body.decode('utf-8'))