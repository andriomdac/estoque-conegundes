def serialize_product(product):
    """
    Transform a product instance from a model to json
    """
    return {
        "id": product.pk,
        "name": product.name,
        "brand": product.brand.name,
        "barcode": product.barcode,
    }