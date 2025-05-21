from .models import PaymentMethodChoice

def validate_method_id(method_id):
    try:
        method_id = int(method_id)
    except(ValueError, TypeError):
        raise ValueError("'method' (ID) field must be an integer.")
    if not PaymentMethodChoice.objects.filter(id=method_id).exists():
        raise PaymentMethodChoice.DoesNotExist(f"'method' of id {method_id} does not exist.")
    
    return PaymentMethodChoice.objects.get(id=method_id)