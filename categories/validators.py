from .models import Category
from app.utils.exceptions import DuplicateCategoryException

def validate_category(category_id):
    try:
        category = Category.objects.get(id=int(category_id))
        return category
    except Category.DoesNotExist:
        raise Category.DoesNotExist(f"Category '{category_id}' does not exist")
    except (ValueError, TypeError):
        raise ValueError("Category ID must be a valid integer.")
    