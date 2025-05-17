from store_items.models import StoreItem

def validate_store_item(store_item):
    if StoreItem.objects.filter(store=store_item.store, product=store_item.product).exists():
        raise ValueError(f"store '{store_item.store.pk}' already has this product '{store_item.product.pk}'")
    return store_item