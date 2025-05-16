def serialize_category(category):
    """
    Transform a category instance from a model to json
    """
    return {
        "id": category.pk,
        "name": category.name
    }