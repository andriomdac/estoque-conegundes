from decimal import Decimal, InvalidOperation, ROUND_HALF_UP

def validate_store_item_price(store_item):
    return store_item

def validate_cost_price(cost_price):
    if not cost_price:
        raise ValueError("'cost_price' cannot be blank.")
    try:
        cost_price = Decimal(str(cost_price)).quantize(Decimal("0.00"), rounding=ROUND_HALF_UP)
    except InvalidOperation:
        raise ValueError("'cost_price' must be a decimal")
    return str(cost_price)

def validate_selling_price(selling_price):
    if not selling_price:
        raise ValueError("'selling_price' cannot be blank.")
    try:
        selling_price = Decimal(str(selling_price)).quantize(Decimal("0.00"), rounding=ROUND_HALF_UP)
    except InvalidOperation:
        raise ValueError("'selling_price' must be a decimal")
    return str(selling_price)