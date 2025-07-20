from django.urls import path
from sale_items.views import (
    sale_item_create_list_view, sale_item_update_detail_delete_view
)


urlpatterns = [
    path('', sale_item_create_list_view, name='sale_item_create_list'),
    path('<int:sale_item_id>/', sale_item_update_detail_delete_view, name='sale_item_update_detail_delete'),

]