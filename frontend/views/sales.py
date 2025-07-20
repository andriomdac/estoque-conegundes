from django.shortcuts import render
from frontend.utils.decorators import token_required
from ..utils.api_requests import get_sales_list
from icecream import ic



@token_required
def sales_list_view(request):
    sales = get_sales_list(request)
    return render(
        request=request,
        template_name='sales/sales_list.html',
        context={"sales": sales}
        )