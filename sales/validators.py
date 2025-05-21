from .models import Sale
from decimal import Decimal, InvalidOperation,  ROUND_HALF_UP


def validate_sale_id(sale_id):
    try:
        sale_id = int(sale_id)
    except (ValueError, TypeError):
        raise ValueError("'sale' (ID) field must be an integer.")
    if not Sale.objects.filter(id=sale_id).exists():
        raise Sale.DoesNotExist(f"Sale of if {sale_id} does not exist.")
    
    return Sale.objects.get(id=sale_id)


def validate_total_amount(total_amount):
    if not total_amount:
        raise ValueError("'total_amount' cannot be blank.")
    try:
        total_amount = Decimal(str(total_amount)).quantize(Decimal("0.00"), rounding=ROUND_HALF_UP)
    except InvalidOperation:
        raise ValueError("'total_amount' must be a decimal")
    return str(total_amount)