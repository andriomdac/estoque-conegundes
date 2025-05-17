from app.utils.exceptions import DuplicateBarcodeException, DuplicateProductException
from .models import Product


def validade_barcode(barcode):
    try:
        barcode = int(barcode)
    except (ValueError, TypeError):
        raise ValueError("'barcode' must be only numbers.")
    if Product.objects.filter(barcode=barcode).exists():
        raise ValueError("Product with this barcode already exists.")
    return barcode


def validate_product_name(name, brand):
    try:
        if Product.objects.filter(name=name, brand=brand).exists():
            raise DuplicateProductException()
    except (ValueError, TypeError):
        raise ValueError("Name must be a string")
    except DuplicateProductException:
        raise DuplicateProductException()
    return name


def validate_product(product_id):
    try:
        product_id = int(product_id)
    except TypeError:
        raise ValueError("'product' (ID) must be an integer.")
    if not Product.objects.filter(id=product_id).exists():
        raise Product.DoesNotExist("Product with this ID does not exist.")
    return Product.objects.get(id=product_id)