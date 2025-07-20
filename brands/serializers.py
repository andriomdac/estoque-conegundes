def serialize_brand(brand):
    """
    Transform a brand instance from a model to json
    """
    return {
        "id": brand.pk,
        "name": brand.name
    }