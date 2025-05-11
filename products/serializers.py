def serialize_product(product):
    """
    Transform a product instance from a model to json
    """
    return {
        "id": product.pk,
        "name": product.name,
        "brand": {
            "id": product.brand.pk,
            "name": product.brand.name
        },
        "barcode": product.barcode,
    }


def serialize_brand(brand):
    """
    Transform a brand instance from a model to json
    """
    return {
        "id": brand.pk,
        "name": brand.name
    }