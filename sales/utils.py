from .models import Sale
from app.utils.http import build_json_response
from .serializers import serialize_sale


def create_new_sale(request, response):
    """
    Create (POST) new sale
    """
    new_sale = Sale.objects.create()
    
    return build_json_response(response, serialize_sale(new_sale), 201)