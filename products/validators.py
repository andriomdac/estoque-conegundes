from app.utils.exceptions import FieldValidationError
from .models import Product


def validade_barcode(barcode):
    try:
        barcode = int(barcode)
    except (ValueError, TypeError):
        raise FieldValidationError("'barcode' must be only numbers.")
    if Product.objects.filter(barcode=barcode).exists():
        raise FieldValidationError("Product with this barcode already exists.")
    return barcode