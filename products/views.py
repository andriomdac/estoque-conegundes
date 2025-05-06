from django.shortcuts import render
from .models import Product
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Brand
from django.shortcuts import get_object_or_404
from django.db import IntegrityError
from .utils import (
    convert_product_instance_to_json,
    exception_to_json,
    get_json_from_request_body
)


@csrf_exempt
def product_create_list_view(request):
    """
    GET list of products or POST a new product
    """
    response = []

    if request.method == 'GET':
        products = Product.objects.all()

        for product in products:
            response.append(convert_product_instance_to_json(product))

        return JsonResponse(response, safe=False, status=200)
    
    if request.method == 'POST':
        try:
            request_body = get_json_from_request_body(request)
            #Get all fields from request body
            name = request_body.get('name')
            brand = Brand.objects.get(id=request_body.get('brand'))
            barcode = request_body.get('barcode')

            new_product = Product.objects.create(
                name = name,
                brand = brand,
                barcode = barcode
            )

            new_product.full_clean()
            new_product.save()
            
            response.append(convert_product_instance_to_json(new_product))
            return JsonResponse(response, safe=False, status=201)

        except Exception as e:
            response.append(exception_to_json(e))
            return JsonResponse(response, safe=False, status=400)

    
    #If any other method, return 405
    response.append({"error": "Method not allowed"})
    return JsonResponse(response, safe=False, status=405)


@csrf_exempt
def product_update_detail_delete_view(request, product_id):
    """
    GET, UPDATE or DELETE a product
    """

    response = []

    if request.method == 'GET':
        try:
            product = Product.objects.get(id=product_id)
            response.append(convert_product_instance_to_json(product))
            return JsonResponse(response, safe=False, status=200)

        except Exception as e:
            response.append(exception_to_json(e))
            return JsonResponse(response, safe=False, status=400)

    if request.method == 'PUT':
        try:
            product = Product.objects.get(id=product_id)
            updated_product = get_json_from_request_body(request)

            product.name = updated_product.get("name", product.name)
            product.barcode = updated_product.get("barcode", product.barcode)
            product.brand = Brand.objects.get(id=int(updated_product.get("brand")))

            product.save()
            response.append(convert_product_instance_to_json(product))
            return JsonResponse(response, safe=False, status=204)

        except Exception as e:
            response.append(exception_to_json(e))
            return JsonResponse(response, safe=False, status=400)

    if request.method == 'DELETE':
        try:
            product = Product.objects.get(id=product_id)
            product.delete()
            return JsonResponse(response, safe=False, status=204)
        except Exception as e:
            response.append(exception_to_json(e))
            return JsonResponse(response, safe=False, status=400)

    #If any other method, return 405
    response.append({"error": "Method not allowed"})
    return JsonResponse(response, safe=False, status=405)