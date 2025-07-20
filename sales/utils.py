from .models import Sale
from app.utils.http import build_json_response, build_json_error_response
from .serializers import serialize_sale
from app.utils.exceptions import ObjectValidationError 
from django.core.validators import ValidationError
from icecream import ic

def create_new_sale(request, response):
    """
    Create (POST) new sale
    """
    new_sale = Sale.objects.create() 
    return build_json_response(response, serialize_sale(new_sale), 201)


def update_sale_total_amount(sale):
	try:
		payments_total = 0
		for payment in sale.payment_methods.all():
			payments_total += payment.total_amount 
		
		sale.total_amount = payments_total
		sale.full_clean()
		sale.save()
	except ValidationError as e:
		raise ObjectValidationError(e)


def finalize_sale(response, sale_id):
	sale = Sale.objects.get(id=sale_id)
	sale.active = False # All deactivated sales (active=False) are finalized/finished sales

	sale.full_clean()
	sale.save() 
	return build_json_response(response, serialize_sale(sale), 200)


def activate_sale(response, sale_id):
	sale = Sale.objects.get(id=sale_id)
	sale.active = True # All activated sales (active=True) are open/unfinished sales

	sale.full_clean()
	sale.save()
	return build_json_response(response, serialize_sale(sale), 200)
