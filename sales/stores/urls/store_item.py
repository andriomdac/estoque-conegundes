from django.urls import path
from stores.views.store_item import (
    store_item_create_list_view,
    store_item_update_detail_delete_view,
    )


urlpatterns = [
    #Store
    path('', store_item_create_list_view, name='store_item_create_list'),
    path('<int:store_item_id>/', store_item_update_detail_delete_view, name='store_item_update_detail_delete'),
]