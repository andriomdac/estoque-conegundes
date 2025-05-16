from .models import Brand
from app.utils.exceptions import DuplicateBrandException

def validate_brand(brand_id):
    try:
        brand = Brand.objects.get(id=int(brand_id))
        return brand
    except Brand.DoesNotExist:
        raise Brand.DoesNotExist(f"Brand '{brand_id}' does not exist")
    except (ValueError, TypeError):
        raise ValueError("Brand ID must be a valid integer.")
    