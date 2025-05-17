from .models import Category

def validate_category(category_id):
    try:
        category_id = int(category_id)
        category = Category.objects.get(id=int(category_id))
    except Category.DoesNotExist:
        raise Category.DoesNotExist(f"Category '{category_id}' does not exist")
    except (ValueError, TypeError):
        raise ValueError("Category ID must be a valid integer.")
    return Category.objects.get(id=category_id)
    

def validate_category_name(name):
    if Category.objects.filter(name=name).exists():
        raise ValueError("Category with this name already exists.")
    return name
