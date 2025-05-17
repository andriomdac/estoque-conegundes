def serialize_store(store):
    """
    Convert a Store instance to a JSON-serializable dict.
    """
    return {
        "id": store.pk,
        "name": store.name,
        "active": store.active,
    }