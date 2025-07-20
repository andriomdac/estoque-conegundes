from django.shortcuts import render
from frontend.utils.api_requests import get_store_items_list
from frontend.utils.decorators import token_required
from icecream import ic


@token_required
def store_items_list_view(request):
    store_items = get_store_items_list(request)
    ic(store_items)
    return render(request, "store_items/store_items_list.html", context={"store_items": store_items})