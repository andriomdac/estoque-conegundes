from .models import Store
from app.utils.exceptions import DuplicateStoreException


def validate_store_name(name):
    if not str(name).strip():
        raise ValueError("'name' can't be blank.")
    if Store.objects.filter(name=name).exists():
        raise DuplicateStoreException()
    return name


def validate_store(store_id):
    try:
        store_id = int(store_id)
    except (TypeError):
        raise ValueError("'store' (ID) must be an integer.")
    if not Store.objects.filter(id=store_id).exists():
        raise Store.DoesNotExist("Store does not exist.")
    return Store.objects.get(id=store_id)