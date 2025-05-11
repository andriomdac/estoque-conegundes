from django.urls import path
from stores.views.price import (
    price_create_list_view,
    price_detail_delete_view,
    )


urlpatterns = [
    path('', price_create_list_view, name='price_create_list'),
    path('<int:price_id>/', price_detail_delete_view, name='price_detail_delete'),
]