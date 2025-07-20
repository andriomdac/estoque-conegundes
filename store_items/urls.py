from django.urls import path
from store_items.views import (
    store_item_create_list_view,
    store_item_update_detail_delete_view,
    )


urlpatterns = [
    path('', store_item_create_list_view, name='store_item_create_list'),
    path('<int:store_item_id>/', store_item_update_detail_delete_view, name='store_item_update_detail_delete'),
]